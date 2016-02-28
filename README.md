# RoboPy
A little Python robot game where players code AIs to compete against each other. Inspired by
[Robocode](http://robocode.sourceforge.net/). This game would be a fun way for introductory programmers to learn (because Robots+Python).

## Installation
Install the dependencies:
```
pip install -r requirements.txt
```
Then clone this Repo.

### Requirements
- Python 3.5-ish
- [Pyglet](https://bitbucket.org/pyglet/pyglet/wiki/Home)

## Running
After the installation is complete. Switch to the RoboPy directory and run `python run.py`.

## Developing
If you'd like to help, just fork the repo, make your changes, and make a pull request.

### Architecture Notes
- Stock Robots will be built in the game.Robots module and should have a module of their own name (I.e. the BasicBot is in the game.Robots.BasicBot module)
- Everything else is in the works.
