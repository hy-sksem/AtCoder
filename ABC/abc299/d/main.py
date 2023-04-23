def interactive(x):
    print("?", x)
    return int(input())


N = int(input())

L, R = 1, N - 1

while L < R:
    mid = (L + R + 1) // 2
    out = interactive(mid)
    if out == 0:
        L = mid
    else:
        R = mid - 1
print("!", L)
