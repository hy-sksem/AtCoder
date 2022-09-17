N, M = map(int, input().split())
C = list(map(int, input().split()))

dp = [10**18] * (N + 1)
dp[0] = 0
for c in C:
    for i in range(c, N + 1):
        dp[i] = min(dp[i], dp[i - c] + 1)
print(dp[N])
