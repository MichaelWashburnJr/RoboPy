import math

def is_circle_collision(c1, c2):
    """
    Check if there is a collision between two circles c1 and c2.
    Returns True if there is a collision.
    """
    # Find the distance between c1 and c2's origins
    dx = c2.x - c1.x
    dy = c2.y - c1.y
    dist = math.sqrt( (dx**2) + (dy**2) )
    # If the length of the combined radii is less than the distance, there is a collision
    return (c1.radius + c2.radius) <= dist
