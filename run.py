import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import pyglet
from game import Game



game = Game()
window = pyglet.window.Window(width=game.width, height=game.height)

@window.event
def on_draw():
    pyglet.gl.glClearColor(*(255,255,255,255))
    window.clear()
    game.draw()

x = [70, 570, 570, 70]
y = [410, 410, 70, 70]
i = 0

game.bot.object.x = 100
game.bot.object.y = 100
game.bot.object.move_to_point(300,300)

while True:
    pyglet.clock.tick()

    for window in pyglet.app.windows:
        window.switch_to()
        window.dispatch_events()
        window.dispatch_event('on_draw')
        window.flip()

    game.bot.object.process_events()
    sys.stdout.flush()
