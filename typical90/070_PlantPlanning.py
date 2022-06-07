N = int(input())
X, Y = [], []
for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
X.sort()
Y.sort()
ans = 0
for i in range(N):
    ans += abs(X[i] - X[N // 2]) + abs(Y[i] - Y[N // 2])
print(ans)
