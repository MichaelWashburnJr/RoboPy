from .events import TurnEvent, LinearMoveEvent
import math

class Object:
    """A Game Object which can move and stuff"""

    def __init__(self, **kwargs):
        # Speed the object travels in pixels per second
        self.x = kwargs.get('x', 0)
        self.y = kwargs.get('y', 0)
        self.speed = kwargs.get('speed', 2)            # Pixels/Second
        self.turn_speed = kwargs.get('turn_speed', 0.1)  # Radians/Second
        self.angle = kwargs.get('angle', 0)             # Radians
        self.async_events = []
        self.sync_events = []

    def add_async_event(self, event):
        """
        Add an event to the asynchronous event list. Events in this list will execute
        at the same time until they are done.
        """
        self.async_events.append(event)

    def add_sync_event(self, event):
        """
        Add an event to the synchronous event list. Events in this list will execute one
        at a time, waiting until the previous event is done to process the next event.
        """
        self.sync_events.append(event)

    def process_events(self):
        """Call the Action method of the event and update the event queue."""
        # Process the async events first
        for event in self.async_events:
            event.do_work()
            if event.is_done():
                self.async_events.remove(event)
        # Process sync events
        for event in self.sync_events:
            event.do_work()
            print(event)
            if not event.is_done():
                break
            else:
                self.sync_events.remove(event)
                print(self.angle)

    def move_forward(self, distance, async=False):
        """Move the object a distance in a line."""
        if async:
            self.add_async_event(LinearMoveEvent(self, distance))
        else:
            self.add_sync_event(LinearMoveEvent(self, distance))

    def turn(self, radians, async=False):
        """Turn the object a number of radians"""
        if async:
            self.add_async_event(TurnEvent(self, radians))
        else:
            self.add_sync_event(TurnEvent(self, radians))

    def face_point(self, x, y, async=False):
        """turn to face the point (x,y)"""
        # Find the angle between this robot and the point
        dx = x - self.x
        dy = y - self.y
        rads = math.atan2(-dy, dx)
        rads %= 2*math.pi
        # See if it is easier to go clocwise or counter clockwise
        cw = (rads - self.angle) % (2*math.pi)
        ccw = (self.angle - rads) % (2*math.pi)
        # turn the inner object
        if cw <= ccw:
            self.turn(cw, async)
        else:
            self.turn(-ccw, async)

    def move_to_point(self, x, y):
        """Turn and face the point (x,y), then move to it."""
        self.face_point(x,y)
        # Find the distance between this point and (x,y)
        dx = x - self.x
        dy = y - self.y
        d = math.sqrt( (dx**2) + (dy**2) )
        # Move that distance
        self.move_forward(d)
