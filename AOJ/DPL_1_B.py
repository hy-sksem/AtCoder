N, W = map(int, input().split())
dp = [[-1] * (W + 1) for _ in range(N + 1)]
for i in range(W + 1):
    dp[0][i] = 0

for i in range(1, N + 1):
    v, w = map(int, input().split())
    for j in range(W + 1):
        if j - w >= 0:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[N][W])
