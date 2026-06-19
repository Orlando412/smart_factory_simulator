from enum import Enum
"""Represents the different states of a machine.""" 
class MachineState(Enum):
    STAND_BY = "STAND BY"
    READY = "READY"
    RUN = "RUN"
    ERROR = "ERROR"