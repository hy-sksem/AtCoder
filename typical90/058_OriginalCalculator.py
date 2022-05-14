def digit_sum(x: int) -> int:
    ans = 0
    while x > 0:
        ans += x % 10
        x //= 10
    return ans


N, K = map(int, input().split())
mod = 10**5
dp = [[0] * (10**5) for _ in range(60)]

for i in range(10**5):
    dp[0][i] = (digit_sum(i) + i) % mod

for i in range(1, 60):
    for j in range(10**5):
        dp[i][j] = dp[i - 1][dp[i - 1][j]]

ans = N
for i in range(60):
    if K >> i & 1:
        ans = dp[i][ans]

print(ans)
