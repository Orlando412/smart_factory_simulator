import time   
from simulator.machine import MachineSimulator
from communication.events import EventBus , Event
from simulator.machine import MachineSimulator

event_bus = EventBus()
machine = MachineSimulator(event_bus)

try:

    while True:

        machine.run_cycle()

        time.sleep(1)

except KeyboardInterrupt:

    print("\nSimulation Stopped")
    
    machine.print_analytics_report()