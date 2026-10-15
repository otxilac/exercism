import math

def score(x: float, y: float) -> int:
    """Given a point in the target (defined by its Cartesian coordinates x and y,             where x and y are real), calculate the correct score earned by a dart landing
        at that point.
    """
    distance = math.sqrt(x**2 + y**2)
    if distance > 10:
        return 0
    elif distance > 5:
        return 1
    elif distance > 1:
        return 5
    else:
        return 10
