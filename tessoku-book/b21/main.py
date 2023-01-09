N = int(input())
S = int(input())

dp = [[-1] * N for _ in range(N)]

for i in range(N):
    dp[i][i] = 1

for i in range(N - 1):
    if S[i] == S[i + 1]:
        dp[i][i + 1] = 2
    else:
        dp[i][i + 1] = 1

for length in range(2, N):
    for l in range(N - length):
        r = l + length
        if S[l] == S[r]:
            dp[l][r] = max(dp[l][r - 1], dp[l + 1][r], dp[l + 1][r + 1] + 2)
        else:
            dp[l][r] = max(dp[l][r - 1], dp[l + 1][r])

print(dp[0][N - 1])
