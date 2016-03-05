from .event import Event
import math
import time

class LinearMoveEvent(Event):
    """An event to move an object"""

    def __init__(self, object, distance):
        """
        Params:
            - object: the object that is moving
            - distance: the distance to move
            - angle: the angle to move the object at (radians)
        The object will be moved 'distance' pixels at 'angle' radians.
        """
        super().__init__()
        self.object = object
        self.target_dist = distance
        self.cur_dist = 0
        self.last_process = time.clock()
        self.speed = self.object.speed
        # if the distance is negative, change speed to be negative
        if distance < 0:
            self.speed *= -1


    def do_work(self):
        """
        Move the object a distance based on the time lapsed since the last process.
        """
        # Find the delta in time since the last process
        dt = time.clock() - self.last_process
        # Find the distance to move the object based on the speed and dt
        d = self.speed * dt
        # Check to make sure we do not overshoot the target
        if abs(self.cur_dist + d) > abs(self.target_dist):
            d = self.target_dist - self.cur_dist
        dx = d * math.cos(self.object.angle)
        dy = d * -math.sin(self.object.angle)
        self.cur_dist += dx
        # move the object
        self.object.x += dx
        self.object.y += dy

    def is_done(self):
        """Return true if the distance has been traveled"""
        print(str(self.cur_dist) + " : " + str(self.target_dist))
        return self.cur_dist == self.target_dist

    def __str__(self):
        return "LinearMoveEvent(distance=%f)" % (self.target_dist)

    def __repr__(self):
        return self.__str__()
