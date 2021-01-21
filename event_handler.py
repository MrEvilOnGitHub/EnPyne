class BaseError(Exception):
    """Base exception class for this module"""
    pass

class EventError(BaseError):
    """Exception raised when attempting to add a non-callable event object"""

# Tick system:
# Global & live ticks
# - Global try to update every 1/nth of a seconds
# - live try to update as often as possible
# 
# Events are divided into multiple categories:
# - Active: Update every tick (global or live)
# - Once: Perform event once, then set it to sleep
# - Sleep: don't activate unless explicitly called
# 
# Sub-categories:
# - Input: Triggers on User input when not sleeping
# - Engine: Events to keep the engine working (This includes rendering, physics etc)
# - Object: Events asigned to objects that don't fit into any of the above categories
