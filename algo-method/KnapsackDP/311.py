N, M = map(int, input().split())
A = list(map(int, input().split()))

dp = [[10**18] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(1, N + 1):
    a = A[i - 1]
    for j in range(M + 1):
        if j - a >= 0:
            dp[i][j] = min(dp[i][j], dp[i - 1][j - a] + 1)
        dp[i][j] = min(dp[i][j], dp[i - 1][j])
print(dp[N][M] if dp[N][M] != 10**18 else -1)
