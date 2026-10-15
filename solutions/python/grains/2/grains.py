def square(number) -> int:
    """Returns the number of grains on a given square"""
    if number not in range(1, 65):
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number-1)


def total() -> int:
    """Returns the total number of grains on the chessboard"""
    sum = 0
    for number in range(1, 65):
        sum += square(number)
    return sum
