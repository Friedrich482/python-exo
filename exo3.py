import math


def greatest_root(a: float, b: float, c: float):
    """
    Returns the greatest root of a polynom of the second degree

    :param float a, float b, float c: The three parameters of
    :return: The greatest square if available and None if there is none
    """
    if a == 0:
        if b == 0:
            if c != 0:
                return None
            return math.inf
        return -c / b

    d = b**2 - 4 * a * c
    if d < 0:
        return None
    if d == 0:
        return -b / (2 * a)
    return (-b + math.sqrt(d)) / (2 * a)


assert greatest_root(1, 1, 1) == None
assert greatest_root(1, -2, 1) == 1
assert greatest_root(4, -4, -24) == 3
