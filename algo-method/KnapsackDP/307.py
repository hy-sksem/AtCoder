N = int(input())
A = [0] + list(map(int, input().split()))

dp = [-(10**18)] * (N + 1)
dp[0] = 0
for i in range(1, N + 1):
    dp[i] = max(dp[i - 1], dp[i - 1] + A[i])
print(dp[N])
