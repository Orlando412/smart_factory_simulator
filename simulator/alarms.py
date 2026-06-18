class Alarm:

    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __str__(self):
        return f"[{self.code}] {self.message}"


ALARMS = [
    Alarm("E001", "Conveyor Jam"),
    Alarm("E002", "Sensor Misalignment"),
    Alarm("E003", "Vision Inspection Failure"),
    Alarm("E004", "Emergency Stop")
]