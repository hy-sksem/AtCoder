A, B, C, X, Y = map(int, input().split())
d = X - Y
if d > 0:
    print(min(A + B, 2 * C) * Y + d * min(A, 2 * C))
elif d < 0:
    print(min(A + B, 2 * C) * X + abs(d) * min(B, 2 * C))
else:
    print(min(A + B, 2 * C) * X)
