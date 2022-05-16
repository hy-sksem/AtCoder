N = int(input())
A, B, C = map(int, input().split())

minimum = float("inf")
for i in range(10000):
    for j in range(10000 - i):
        v = N - (i * A + j * B)
        q, mod = divmod(v, C)
        if mod == 0 and v >= 0 and i + j + q <= 9999:
            minimum = min(minimum, i + j + q)
print(minimum)
