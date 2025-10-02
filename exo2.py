from exo1 import F_to_C, C_to_F


def isalmost(n, m, d=1e-13):
    return abs(n - m) < d


[(a, b) for F in range(20) for a, b in [[5 / 9 * (F - 32), 5 * (F - 32) / 9]] if a != b]

assert all(
    isalmost(*(err := a))
    for a in [(1, 1), (1, 1.1, 0.1)] + [(n, n - 1e-13) for n in range(1, 100)]
), err

assert not any(
    isalmost(*(err := a))
    for a in [(1, 2), (1, 1.1), (5, 5.00008)] + [(n, n - 1e-12) for n in range(1, 100)]
), err

assert isalmost(F_to_C(-459.67), -273.15)
assert isalmost(C_to_F(-273.15), -459.67)
assert all(
    isalmost(efc := F_to_C(C_to_F(c)), ec := c)
    and isalmost(efc := C_to_F(F_to_C(c)), c)
    for c in range(-273, 200)
), (ec, efc)
