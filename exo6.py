def g(x: float):
    return x**2 - 2


def di(f: function, a: float, b: float, d=1e-16):
    if abs(a - b) < d:
        return

    m = abs((a - b) / 2)
