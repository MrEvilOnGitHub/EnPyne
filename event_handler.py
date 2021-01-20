class BaseError(Exception):
    """Base exception class for this module"""
    pass

class EventError(BaseError):
    """Exception raised when attempting to add a non-callable event object"""

# Just some dummy events
def _dummy1():
    print("Dummy1")

def _dummy2():
    print("Dummy2")

# List of all events added to the handler (+base ones)
all_events = [2, _dummy1, _dummy2]

# list of each event's status. index matching
event_status = [2, "repeat","do_once"]

# List of each event's type, index matching above lists
event_type = [2, "update", "input"]

# Add events to the event caller
def add_event(func, status, e_type):
    if callable(func):
        all_events.append(func)
        event_status.append(status)
        event_type.append(e_type)
    else:
        raise EventError

def caller():
    for i in range(len(all_events)):
        # Just call the object function for now. Stuff them into individual threads later on
        if event_status[i] == "repeat":
            all_events[i]()
        elif event_status[i] == "do_once":
            all_events[i]()
            event_status[i] = "sleep"
