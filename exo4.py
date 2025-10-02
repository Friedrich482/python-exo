from math import sqrt


def roots(a: float, b: float, c: float):
    if a == 0:
        if b == 0:
            if c != 0:
                return ()
            return ()
        return (-c / b,)

    d = b**2 - 4 * a * c
    if d < 0:
        return ()
    if d == 0:
        return (-b / (2 * a),)
    return ((-b + sqrt(d)) / (2 * a), (-b - sqrt(d)) / (2 * a))


assert roots(1, 1, 1) == ()
assert roots(1, -2, 1) in [(1, 1), (1,)]
assert set(roots(4, -4, -24)) == {-2, 3}
