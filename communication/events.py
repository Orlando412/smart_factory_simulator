class Event:
    """Represents an event in the system."""

    def __init__(self, event_type, payload):
        self.event_type = event_type
        self.payload = payload

    def __str__(self):
        return f"{self.event_type}: {self.payload}"


class EventBus:

    def __init__(self):
        self.events = []

    def publish(self, event):
        self.events.append(event)
        print(f"[EVENT] {event}")

    def get_events(self):
        return self.events

    def clear(self):
        self.events.clear()