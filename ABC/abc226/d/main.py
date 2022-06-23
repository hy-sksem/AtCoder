from math import gcd

N = int(input())
X = []
Y = []
for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

ans = set()

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        xd, yd = X[i] - X[j], Y[i] - Y[j]
        g = gcd(xd, yd)
        ans.add((xd // g, yd // g))
print(len(ans))
