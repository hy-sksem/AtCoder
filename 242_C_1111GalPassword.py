N = int(input())

MOD = 998244353
dp = [[0] * 10 for _ in range(N + 1)]
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N + 1):
    for j in range(1, 10):
        for k in range(max(1, j - 1), min(10, j + 2)):
            dp[i][k] += dp[i - 1][j]
            dp[i][k] %= MOD
ans = 0
for i in range(1, 10):
    ans += dp[N][i]
    ans %= MOD
print(ans)
