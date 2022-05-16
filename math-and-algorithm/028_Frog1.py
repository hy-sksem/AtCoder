N = int(input())
H = list(map(int, input().split()))

dp = [0 for i in range(N)]
dp[0] = 0
for i in range(1, N):
    if i > 1:
        dp[i] = min(dp[i - 1] + abs(H[i] - H[i - 1]), dp[i - 2] + abs(H[i] - H[i - 2]))
    else:
        dp[i] = dp[i - 1] + abs(H[i] - H[i - 1])
print(dp[-1])
