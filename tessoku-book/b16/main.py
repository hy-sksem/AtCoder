N = int(input())
h = list(map(int, input().split()))

dp = [10**18] * N
dp[0], dp[1] = 0, abs(h[0] - h[1])

for i in range(2, N):
    dp[i] = min(dp[i - 1] + abs(h[i - 1] - h[i]), dp[i - 2] + abs(h[i - 2] - h[i]))
print(dp[-1])
