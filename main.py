import time   
from simulator.machine import MachineSimulator
from communication.events import EventBus , Event
from simulator.machine import MachineSimulator
from simulator.factory import Factory
from database.schema import initialize_database
from database.historian import Historian

initialize_database()
historian = Historian()
event_bus = EventBus(historian)
factory = Factory(event_bus)


try:

    while True:

        
        factory.run_cycle()

        time.sleep(1)

except KeyboardInterrupt:

    print("\nSimulation Stopped")
    print()

    print("Database Summary")

    print("----------------")

    print(
        historian.total_events(),
        "events recorded."
    )

    print(
        len(historian.alarms()),
        "alarms logged."
    )

    
    factory.print_factory_report()