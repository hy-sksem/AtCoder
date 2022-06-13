import math


def int1(x: int) -> int:
    return int(x) - 1


N, K = map(int, input().split())
A = list(map(int1, input().split()))
X, Y = [], []
for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
ans = 0

for i in range(N):
    if i in A:
        continue
    temp = float("inf")
    for a in A:
        x = X[a]
        y = Y[a]
        # print(math.sqrt((x - X[i]) ** 2 + (y - Y[i]) ** 2))
        temp = min(temp, math.sqrt((x - X[i]) ** 2 + (y - Y[i]) ** 2))
        # print("x:", x, "y:", y, "i:", i, "temp:", temp)
    ans = max(ans, temp)

print(ans)
