N = int(input())
a = list(map(int, input().split()))
mod = 998_244_353

ans = 0
for i in range(1, N + 1):
    dp = [[0] * i for _ in range(i + 1)]
    dp[0][0] = 1
    for j in range(N):
        x = a[j] % i
        for k in range(i, 0, -1):
            for l in range(i):
                if dp[k - 1][l]:
                    dp[k][(l + x) % i] += dp[k - 1][l]
                    dp[k][(l + x) % i] %= mod
    ans += dp[-1][0]
    ans %= mod
print(ans)
