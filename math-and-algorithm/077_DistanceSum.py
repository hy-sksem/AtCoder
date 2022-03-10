N = int(input())
X = [0 for i in range(N)]
Y = [0 for i in range(N)]
for i in range(N):
    X[i], Y[i] = map(int, input().split())

X.sort()
Y.sort()

ans = 0
for i in range(1, N + 1):
    ans += X[i - 1] * (-N + 2 * i - 1)
    ans += Y[i - 1] * (-N + 2 * i - 1)
print(ans)
