class Event():
    """Interface for declaring events"""

    def __init__(self):
        pass

    def do_work(self):
        """Processes a piece of work for this event"""
        pass

    def is_done(self):
        """Returns true when this event has been completed"""
        pass
