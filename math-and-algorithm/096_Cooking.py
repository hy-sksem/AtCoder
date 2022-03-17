N = int(input())
T = list(map(int, input().split()))

sumT = sum(T)
dp = [[False] * (sumT + 1) for _ in range(N + 1)]
dp[0][0] = True

for i in range(1, N + 1):
    for j in range(sumT + 1):
        if j < T[i - 1]:
            if dp[i - 1][j]:
                dp[i][j] = True
            else:
                dp[i][j] = False
        if j >= T[i - 1]:
            if dp[i - 1][j] or dp[i - 1][j - T[i - 1]]:
                dp[i][j] = True
            else:
                dp[i][j] = False

ans = 10**10
for i in range(sumT + 1):
    if dp[N][i]:
        cooking_time = max(i, sumT - i)
        ans = min(ans, cooking_time)
print(ans)
