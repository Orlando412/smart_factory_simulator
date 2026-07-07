from simulator.machine import MachineSimulator


class Factory:
    """
    Manages multiple machines within a factory.
    """

    def __init__(self, event_bus):

        #self.name = name
        self.machines = [
            MachineSimulator(event_bus, "Machine-01"),
            MachineSimulator(event_bus, "Machine-02"),
            MachineSimulator(event_bus, "Machine-03")
        ]

        self.machines[0].quality_rate = 0.95
        self.machines[1].quality_rate = 0.90
        self.machines[2].quality_rate = 0.85


    def print_factory_report(self):

        print("\n========== FACTORY REPORT ==========")

        factory_oee = round(
            sum(
                machine.oee_history[-1]
                if machine.oee_history else 0
                for machine in self.machines
            ) / len(self.machines),
            2
        )

        print(
            f"Factory Average OEE: "
            f"{factory_oee}%"
        )

        total_units = sum(
            machine.units_processed
            for machine in self.machines
        )

        total_good = sum(
            machine.good_units
            for machine in self.machines
        )

        total_bad = sum(
            machine.bad_units
            for machine in self.machines
        )

        print(f"Total Units: {total_units}")
        print(f"Good Units: {total_good}")
        print(f"Bad Units: {total_bad}")

        print("\nMachine Ranking:")

        ranked = sorted(
            self.machines,
            key=lambda m: m.good_units,
            reverse=True
        )

        for machine in ranked:

            print(
                f"{machine.name}: "
                f"{machine.good_units} good units"
            )


        bottleneck = max(
            self.machines,
            key=lambda m: m.get_average_cycle_time()
        )

        print("\nPotential Bottleneck")
        print(f"Machine: {bottleneck.name}")
        print("Reason: Highest Average Cycle Time")
        print(f"Average Cycle Time: {bottleneck.get_average_cycle_time()} sec")

        print("\nUtilization Ranking:")
        util_rank = sorted(
            self.machines,
            key=lambda m:
                m.get_utilization(),
            reverse=True
        )

        for machine in util_rank:
            print(
                f"{machine.name}"
                f" : {machine.get_utilization()}%"
            )

        print("\nOEE Ranking:")

        oee_rank = sorted(
            self.machines,
            key=lambda m:
                m.oee_history[-1]
                if m.oee_history else 0,
            reverse=True
        )

        for machine in oee_rank:

            current_oee = (
                machine.oee_history[-1]
                if machine.oee_history else 0
            )

            print(
                f"{machine.name}: {current_oee:.2f}%"
            )


        print("===================================")

    def run_cycle(self):

        for machine in self.machines:
            machine.run_cycle()