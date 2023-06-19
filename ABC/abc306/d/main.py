N = int(input())
XY = [0] + [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (N + 2) for _ in range(4)]
INF = 10**18

for i in range(1, N + 1):
    x, y = XY[i]
    if x == 1:
        dp[0][i] = -INF
        dp[1][i] = max(dp[0][i - 1], dp[1][i - 1])
        dp[2][i] = max(dp[0][i - 1], dp[1][i - 1]) + y
        dp[3][i] = max(dp[2][i - 1], dp[3][i - 1])
    else:
        dp[0][i] = max(dp[0][i - 1], dp[1][i - 1], dp[2][i - 1], dp[3][i - 1]) + y
        dp[1][i] = max(dp[0][i - 1], dp[1][i - 1])
        dp[2][i] = -INF
        dp[3][i] = max(dp[2][i - 1], dp[3][i - 1])
print(max(dp[0][N], dp[1][N], dp[2][N], dp[3][N]))
