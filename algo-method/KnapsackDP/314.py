S = input()
T = input()

dp = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]
dp[0][0] = 0

for i, s in enumerate(S):
    for j, t in enumerate(T):
        if s == t:
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + 1)
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i + 1][j], dp[i][j + 1])
print(dp[-1][-1])
