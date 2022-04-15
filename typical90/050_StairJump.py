# https://atcoder.jp/contests/typical90/tasks/typical90_ax

N, L = map(int, input().split())
dp = [0] * (N + 1)
dp[0] = 1
mod = 10**9 + 7

for i in range(1, N + 1):
    a = dp[i - 1] if i - 1 >= 0 else 0
    b = dp[i - L] if i - L >= 0 else 0
    dp[i] += a + b
    dp[i] %= mod
print(dp[N])
