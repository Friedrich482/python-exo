from random import randint


class d:
    def __init__(self, N: int):
        self.N = N

    def roll(self):
        return randint(1, self.N)

    def __call__(self):
        return self.roll()

    def __int__(self):
        return int(self.roll())

    def __add__(self, other: int):
        return self.__int__() + other

    def __radd__(self, other: int):
        return other + self.__int__()

    def __sub__(self, other: int):
        return self.__int__() - other

    def __rsub__(self, other: int):
        return other - self.__int__()

    def __mul__(self, other: int):
        return sum([self.__int__() for _ in range(other)])

    def __rmul__(self, other: int):
        return self.__mul__(other)

    def __truediv__(self, other: int):
        return self.__int__() / other

    def __rtruediv__(self, other: int):
        return other / self.__int__()


d6 = d(6)
d20 = d(20)
# print(f"prod is { d6 * 10 }")
# print(f"prod1 is {  10 * d6 }")

print(f"sum and prod is {-100 + 10 * d20 + 40}\n")

from collections import Counter

N = 100000

for v, c in (l := sorted(Counter(3 * (d6 + 0) for _ in range(N)).items())):
    print(f"{v:2} {'=' * (c // 500)}")

print(
    "\navg",
    sum(c * v for v, c in l) / N,
    "\nexpected avg",
    3 / 6 * sum(range(1, 6 + 1)),
    "=",
    3 * (6 + 1) / 2,
)

print(f"Division gives {d6 / 2}")
print(f"RDivision gives {2 / d6}")
print(f"Subtraction gives {d6 - 2}")
print(f"RSubtraction gives {2 - d6}")
