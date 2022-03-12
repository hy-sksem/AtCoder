X = int(input())
S = float("INF")
for i in range(1, 10):
    for d in range(-9, 10):
        b = i
        T = b
        while 0 <= (b + d) < 10 and T < X:
            T = 10 * T + (b + d)
            b += d
        if T >= X:
            S = min(S, T)

print(S)
