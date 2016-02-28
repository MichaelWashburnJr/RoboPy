import pyglet
import os
from math import sin, cos, atan2, radians, degrees, pi

ROBOT_DIR = os.path.dirname(os.path.abspath(__file__))

class BasicBot():
    """
    The Most Basic Robot Implementation. All other Robots should extend this class.
    """

    def __init__(self, **kwargs):
        self.x = kwargs.get('x', 0)
        self.y = kwargs.get('y', 0)
        self.width = 50
        self.height=50
        self.name = kwargs.get('name', "BasicBot")
        self.image = pyglet.image.load(os.path.join(ROBOT_DIR, "robot.png"))
        self.image.anchor_x = self.image.width // 2
        self.image.anchor_y = self.image.height // 2
        self.angle = 0; #0 <= angle < 360
        self.turn_speed = 1 # degrees per move
        # When the bot is X degrees in the right direction it can move forward
        self.turn_move_threshold = 90
        self.speed = 2 # pixels per move

    def turn_to_point(self, x, y):
        """
        Find the angle between the current coordinates and the given point.
        Once found, increment this robots angle towards that point.
        Returns the difference between the target angle and current angle.
        """
        # Find the angle between this robot and the point
        dx = x - self.x
        dy = y - self.y
        r = atan2(-dy, dx)
        r %= 2*pi
        degs = degrees(r)

        if degs != self.angle:
            # See if it is easier to go clocwise or counter clockwise
            cw = (degs - self.angle) % 360
            ccw = (self.angle - degs) % 360

            if cw <= ccw:
                # Turn Clockwise
                if cw >= self.turn_speed:
                    self.angle += self.turn_speed
                else:
                    self.angle = degs
            else:
                # Turn Counter Clockwise
                if ccw > self.turn_speed:
                    self.angle -= self.turn_speed
                else:
                    self.angle = degs
            # Return space between angle and target angle
        return degs - self.angle

    def move_to_point(self, x, y):
        """
        First """
        if (self.x != x) or (self.y != y):
            deg_delta = self.turn_to_point(x,y)
            # If we are in the right direction, start moving
            if deg_delta == 0:
                dx = self.speed * cos(radians(self.angle))
                dy = self.speed * sin(radians(self.angle))
                # Make the move
                if abs(x - self.x) > abs(dx):
                    self.x += dx
                else:
                    self.x = x
                if abs(y - self.y) > abs(dy):
                    self.y -= dy
                else:
                    self.y = y

        # Return True if the robot is at the point
        return (self.x == x) and (self.y == y)




    def sprite(self,**kwargs):
        """Return the Sprite object for this bot at its current position"""
        batch = kwargs.get('batch')
        sprite = None
        if not batch:
            sprite = pyglet.sprite.Sprite(self.image, x=self.x, y=self.y)
        else:
            sprite = pyglet.sprite.Sprite(self.image, x=self.x, y=self.y, batch=batch)
        sprite.rotation = self.angle
        return sprite
