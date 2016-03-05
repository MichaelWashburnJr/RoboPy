from asyncio import Lock

class Arena():
    """
    A class to hold all data relevant to the arena and functionality for maintaining correct
    game state. This includes verifying robot moves.
    """

    def __init__(self):
        bots = []
