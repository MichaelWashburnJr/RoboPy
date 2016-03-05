from .event import Event
import time
import math

class TurnEvent(Event):
    """Turns the object on its axis"""

    def __init__(self, object, radians):
        self.object = object
        # Theta is the change in angle we are turning (radians)
        self.target_theta = radians
        self.cur_theta = 0
        self.last_process = time.clock()
        # The speed at which to turn (radians/second)
        self.speed = object.turn_speed
        # Invert the speed if the turn is negative
        if radians < 0:
            self.speed *= -1


    def do_work(self):
        """
        Turn the object based off of how many seconds have passed since the last time
        the event was processed.
        """
        # Find how long it has been since the last time this ran
        dt = time.clock() - self.last_process
        # Get the max amount of radians we can turn
        r = self.speed * dt
        # Check to make sure we don't overshoot the angle
        if abs(self.cur_theta + r) > abs(self.target_theta):
            print("Here")
            dr = self.target_theta - self.cur_theta
            self.cur_theta += dr
            self.object.angle += dr
        else:
            self.cur_theta += r
            self.object.angle += r
        print(self.object.angle)

    def is_done(self):
        """Return True when the turn is complete"""
        return self.cur_theta == self.target_theta

    def __str__(self):
        return "TurnEvent(radians=%f)" % (self.target_theta)

    def __repr__(self):
        return self.__str__()
