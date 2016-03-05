import pyglet
import os
import math
from game.engine.objects import Circle
from game.engine.physics.collisions import is_circle_collision

ROBOT_DIR = os.path.dirname(os.path.abspath(__file__))

class BasicBot():
    """
    The Most Basic Robot Implementation. All other Robots should extend this class.
    """

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', "BasicBot")
        self.image = pyglet.image.load(os.path.join(ROBOT_DIR, "robot.png"))
        self.image.anchor_x = self.image.width // 2
        self.image.anchor_y = self.image.height // 2
        self.angle = 0; #0 <= angle < 360
        # When the bot is X degrees in the right direction it can move forward
        self.object = Circle(x=kwargs.get('x',0), y=kwargs.get('y',0))

    def sprite(self,**kwargs):
        """Return the Sprite object for this bot at its current position"""
        batch = kwargs.get('batch')
        sprite = None
        if not batch:
            sprite = pyglet.sprite.Sprite(self.image, x=self.object.x, y=self.object.y)
        else:
            sprite = pyglet.sprite.Sprite(self.image, x=self.object.x, y=self.object.y, batch=batch)
        sprite.rotation = math.degrees(self.object.angle)
        return sprite
