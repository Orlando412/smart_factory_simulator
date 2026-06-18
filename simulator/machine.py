import random
import time

from simulator.states import MachineState
from simulator.alarms import ALARMS
from simulator.production import ProductionLot
from simulator.metrics import OEEMetrics


class MachineSimulator:

    def __init__(self):

        self.name = "machine-01"

        self.state = MachineState.STAND_BY

        self.current_alarm = None

        self.current_lot = ProductionLot(
            lot_Id="LOT001",
            quantity=100
        )

        self.good_units = 0
        self.bad_units = 0
        self.units_processed = 0

        self.runtime = 0
        self.downtime = 0

        self.start_time = time.time()

        self.ideal_cycle_time = 1.0

    def run_cycle(self):

        if self.state == MachineState.STAND_BY:
            self.state = MachineState.READY

        elif self.state == MachineState.READY:
            self.state = MachineState.RUN

        elif self.state == MachineState.RUN:

            if random.random() < 0.9:
                self.good_units += 1
            else:
                self.bad_units += 1

            self.units_processed = (
                self.good_units +
                self.bad_units
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

            print("\n----------------------")
            print(f"Machine: {self.name}")
            print(f"State: {self.state.value}")
            print(f"Units: {self.units_processed}")
            print(f"Good: {self.good_units}")
            print(f"Bad: {self.bad_units}")
            print(f"OEE: {oee['oee']}%")
            print("----------------------")

            if random.randint(1, 50) == 1:
                self.current_alarm = random.choice(ALARMS)
                self.state = MachineState.ERROR

        elif self.state == MachineState.ERROR:

            print(f"ALARM: {self.current_alarm}")

            self.downtime += 1

            self.current_alarm = None

            self.state = MachineState.STAND_BY