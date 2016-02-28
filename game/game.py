import pyglet
from threading import Thread
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
        self.bots = [
            BasicBot(x=50, y=50, name="BasicBot1"),
            BasicBot(x=400, y=300, name="BasicBot2")
        ]

    def draw(self):
        """Draw everything on the screen"""
        batch = pyglet.graphics.Batch()
        sprites = []
        for bot in self.bots:
            sprites.append(bot.sprite(batch=batch))
        batch.draw()
