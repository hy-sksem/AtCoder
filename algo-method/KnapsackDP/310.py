N, M = map(int, input().split())
A = list(map(int, input().split()))

dp = [[0] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 1
for i, a in enumerate(A, start=1):
    for j in range(M + 1):
        if j - a >= 0:
            dp[i][j] = dp[i][j] + dp[i - 1][j - a]
        dp[i][j] += dp[i - 1][j]
print(dp[N][M] % 1000)
