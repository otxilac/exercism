def is_triangle(sides: list) -> bool:
    """Checks if the sides provided form a triangle"""
    for side in sides:
        if side <= 0:
            return False
    if sides[0] + sides [1] < sides[2]:
        return False
    elif sides[1] + sides [2] < sides[0]:
        return False
    elif sides[0] + sides [2] < sides[1]:
        return False
    else:
        return True

def equilateral(sides: list) -> bool:
    """Checks if the sides provided form a equilateral triangle"""
    if not is_triangle(sides):
        return False
    if sides[0] == sides[1] and sides[1] == sides[2]:
        return True
    return False


def isosceles(sides: list) -> bool:
    """Checks if the sides provided form a isosceles triangle"""
    if not is_triangle(sides):
        return False
    if sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]:
        return True
    return False


def scalene(sides: list) -> bool:
    """Checks if the sides provided form a scalene triangle"""
    if is_triangle(sides) and not equilateral(sides) and not isosceles(sides):
        return True
    return False
