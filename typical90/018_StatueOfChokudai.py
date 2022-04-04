import math


def query(i):
    PI = math.pi
    cx = 0
    cy = -(L / 2.0) * math.sin(i / T * 2.0 * PI)
    cz = (L / 2.0) - (L / 2.0) * math.cos(i / T * 2.0 * PI)
    d1 = math.sqrt((cx - X) ** 2 + (cy - Y) ** 2)
    d2 = cz
    c = math.atan2(d2, d1)
    return c * 180.0 / PI


T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())


for _ in range(Q):
    e = int(input())
    print(query(e))
