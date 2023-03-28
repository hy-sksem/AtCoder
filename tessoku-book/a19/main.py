N, W = map(int, input().split())
dp = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    w, v = map(int, input().split())
    dp[i][w] = max(dp[i][w], v)
    for j in range(1, W + 1):
        prev = dp[i - 1][j]
        if prev:
            dp[i][j] = max(dp[i][j], prev)
            if j + w <= W:
                dp[i][j + w] = max(dp[i][j + w], prev + v)
print(max(dp[N]))
