S = input()
T = input()

dp = [[-1] * len(S) for _ in range(len(T))]
for i in range(1, len(S) + 1):
    for j in range(1, len(T) + 1):
        if S[i - 1] == T[i - 1]:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + 1)
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len(S)][len(T)])
