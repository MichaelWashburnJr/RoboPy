from .object import Object

class Circle(Object):
    """A Simple Circle object that can be moved around."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        radius = kwargs.get('radius', 0)
