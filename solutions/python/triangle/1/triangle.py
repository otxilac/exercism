def is_triangle(sides: list) -> bool:
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
    if not is_triangle(sides):
        return False
    if sides[0] == sides[1] and sides[1] == sides[2]:
        return True
    return False


def isosceles(sides: list) -> bool:
    if not is_triangle(sides):
        return False
    if sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]:
        return True
    return False


def scalene(sides: list) -> bool:
    if is_triangle(sides) and not equilateral(sides) and not isosceles(sides):
        return True
    return False
