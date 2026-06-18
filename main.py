import time

from simulator.machine import MachineSimulator

machine = MachineSimulator()

try:

    while True:

        machine.run_cycle()

        time.sleep(1)

except KeyboardInterrupt:

    print("\nSimulation Stopped")