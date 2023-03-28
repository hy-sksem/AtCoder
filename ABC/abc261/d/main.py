N, M = map(int, input().split())
X = list(map(int, input().split()))

cy = [0] * (N + 1)

for i in range(M):
    c, y = map(int, input().split())
    cy[c - 1] += y

dp = [[-(10**18)] * (N + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N):
    for j in range(N + 1):
        if j + 1 <= N:
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + X[i] + cy[j])
        dp[i + 1][0] = max(dp[i + 1][0], dp[i][j])

print(max(dp[N]))
