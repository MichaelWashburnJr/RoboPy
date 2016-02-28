import pyglet
from .Robots.BasicBot import BasicBot

class Game():
    """
    Game class for holding the state of the game and managing the arena, robots,
    threads, and provide functionality to the previously mentioned.
    """

    def __init__(self, **kwargs):
        # Grab Values from kwargs
        self.width = kwargs.get('width', 640)
        self.height = kwargs.get('height', 480)

        # Initialize pyglet
        self.bot = BasicBot(x=50, y=50)

    def draw(self):
        """Draw everything on the screen"""
        batch = pyglet.graphics.Batch()
        sprite = self.bot.sprite(batch=batch)
        batch.draw()
