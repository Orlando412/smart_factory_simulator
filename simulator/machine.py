import random
import time
from simulator.states import MachineState
from simulator.alarms import ALARMS
from simulator.production import ProductionLot
from simulator.metrics import OEEMetrics
from communication.events import Event


class MachineSimulator:
    """
        Simulates a manufacturing machine.

        Responsibilities:
         Manage machine state transitions
         Process production units
         Calculate OEE metrics
         Generate alarms
         Publish events to the EventBus
        """

    def __init__(self, event_bus):
        """
        Initialize machine parameters and runtime statistics.

        Args:
            event_bus (EventBus): Central event publisher used
                                  to broadcast machine events.
        """
        self.event_bus = event_bus

        self.name = "machine-01"
        self.state = MachineState.STAND_BY
        self.current_alarm = None
        self.current_lot = ProductionLot(
            lot_Id="LOT001",
            quantity=100
        )

        # Historical analytics
        self.cycle_times = []
        self.oee_history = []
        self.yield_history = []
        self.throughput_history = []
        self.downtime_history = []

        self.good_units = 0
        self.bad_units = 0
        self.units_processed = 0

        self.runtime = 0
        self.downtime = 0

        self.start_time = time.time()

        self.ideal_cycle_time = 1.0

    
    def run_cycle(self):
        """
        Run a single cycle of the machine.
        """
        if self.state == MachineState.STAND_BY:
            self.state = MachineState.READY
            self.event_bus.publish(
                Event(
                    "STATE_CHANGED",
                    {
                        "machine": self.name,
                        "state": self.state.value
                    }
                )
            )

        elif self.state == MachineState.READY:
            self.state = MachineState.RUN
            self.event_bus.publish(
                Event(
                    "STATE_CHANGED",
                    {
                        "machine": self.name,
                        "state": self.state.value
                    }
                )
            )

        elif self.state == MachineState.RUN:

            if random.random() < 0.9:
                self.good_units += 1
            else:
                self.bad_units += 1

            cycle_time = round(
                random.uniform(0.8, 1.3),
                2
            )

            self.cycle_times.append(cycle_time)

            avg_cycle_time = round(
                sum(self.cycle_times) /
                len(self.cycle_times),
                2
            )

            self.units_processed = (
                self.good_units +
                self.bad_units
            )

            self.event_bus.publish(
                Event(
                    "UNIT_PROCESSED",
                    {
                        "machine": self.name,
                        "units_processed": self.units_processed,
                        "good_units": self.good_units,
                        "bad_units": self.bad_units
                    }
                )
            )

            self.runtime += 1

            elapsed = (
                time.time() -
                self.start_time
            )

            oee = OEEMetrics.calculate(
                self.runtime,
                self.downtime,
                self.good_units,
                self.units_processed,
                self.ideal_cycle_time,
                elapsed
            )

            self.oee_history.append(
                oee["oee"]
            )

            throughput = self.units_processed
            self.throughput_history.append(
                throughput
            )



            yield_rate = round(
                (
                    self.good_units /
                    self.units_processed
                ) * 100,
                2
            )

            self.yield_history.append(
                yield_rate
            )

            self.event_bus.publish(
                Event(
                    "OEE_UPDATED",
                    {
                        "machine": self.name,
                        "oee": oee["oee"],
                        "availability": oee["availability"],
                        "performance": oee["performance"],
                        "quality": oee["quality"],
                        "avg_cycle_time": avg_cycle_time,
                        "yield": yield_rate,
                        "throughput": throughput,
                    }
                )
            )

            print("\n----------------------")
            print(f"Machine: {self.name}")
            print(f"State: {self.state.value}")
            print(f"Units: {self.units_processed}")
            print(f"Good: {self.good_units}")
            print(f"Bad: {self.bad_units}")
            print(f"OEE: {oee['oee']}% ")
            print(f"Average Cycle Time: {avg_cycle_time}s ")
            print(f"Yield Rate: {yield_rate}% ")
            print(f"Throughput: {throughput}")
            print("----------------------")

            if random.randint(1, 50) == 1:
                self.current_alarm = random.choice(ALARMS)
                self.event_bus.publish(
                    Event(
                        "ALARM_TRIGGERED",
                        {
                            "machine": self.name,
                            "alarm": str(self.current_alarm)
                        }
                    )
                )
                # self.current_alarm = random.choice(ALARMS)
                self.state = MachineState.ERROR
                self.downtime += 1
    
        elif self.state == MachineState.ERROR:

            print(f"ALARM: {self.current_alarm}")

            self.downtime += 1

            self.event_bus.publish(
                Event(
                    "ERROR_CLEARED",
                    {
                        "machine": self.name,
                        "alarm": str(self.current_alarm)
                    }
                )
            )

            self.downtime_history.append(
                self.downtime
            )

            self.current_alarm = None
            self.state = MachineState.STAND_BY

    def print_analytics_report(self):
        """
        Generate a summary report of machine
        performance collected during simulation.

        Displays:
        - Average cycle time
        - OEE statistics
        - Final yield
        - Total units processed
        """

        print("\n========== ANALYTICS REPORT ==========")
        print(
            f"Average Cycle Time: "
            f"{round(sum(self.cycle_times)/len(self.cycle_times),2)}s"
        )

        print(
            f"Highest OEE: "
            f"{max(self.oee_history):.2f}%"
        )

        print(
            f"Lowest OEE: "
            f"{min(self.oee_history):.2f}%"
        )

        print(
            f"Final Yield: "
            f"{self.yield_history[-1]:.2f}%"
        )

        print(
            f"Total Units: "
            f"{self.units_processed}"
        )
        print("====================================")