from enum import Enum

class MachineState(Enum):
    STAND_BY = "STAND BY"
    READY = "READY"
    RUN = "RUN"
    ERROR = "ERROR"