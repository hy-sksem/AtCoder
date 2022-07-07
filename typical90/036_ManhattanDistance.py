def int1(x: int) -> int:
    return int(x) - 1


N, Q = map(int, input().split())
X = [0] * N
Y = [0] * N
max_X = max_Y = -float("inf")
min_X = min_Y = float("inf")

for i in range(N):
    x, y = map(int, input().split())
    X[i], Y[i] = x + y, x - y
    max_X = max(max_X, X[i])
    max_Y = max(max_Y, Y[i])
    min_X = min(min_X, X[i])
    min_Y = min(min_Y, Y[i])

for i in range(Q):
    q = int1(input())
    ret1 = abs(X[q] - max_X)
    ret2 = abs(X[q] - min_X)
    ret3 = abs(Y[q] - max_Y)
    ret4 = abs(Y[q] - min_Y)
    print(max(ret1, ret2, ret3, ret4))
