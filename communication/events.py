class Event:
    """Represents an event in the system."""

    def __init__(self, event_type, payload):
        self.event_type = event_type
        self.payload = payload

    def __str__(self):
        return f"{self.event_type}: {self.payload}"


class EventBus:
    """Manages the publishing and handling of events."""
    def __init__(self, historian):
        self.events = []
        self.historian = historian

    def publish(self, event):

        self.events.append(event)
        print(f"[EVENT] {event}")
        self.historian.log_event(
            event.payload["machine"],
            event.event_type,
            event.payload
        )


    def get_events(self):
        return self.events

    def clear(self):
        self.events.clear()