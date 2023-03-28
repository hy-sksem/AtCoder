N, W = map(int, input().split())
dp = [[10**18] * (10**5 + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    w, v = map(int, input().split())
    dp[i][v] = min(dp[i][v], w)
    for j in range(1, 10**5 + 1):
        prev = dp[i - 1][j]
        if prev:
            dp[i][j] = min(dp[i][j], prev)
            if j + v <= 10**5:
                dp[i][j + v] = min(dp[i][j + v], prev + w)

ans = 0
for i in range(1, 10**5 + 1):
    if 0 < dp[N][i] <= W:
        ans = max(ans, i)

print(ans)
