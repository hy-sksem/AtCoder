N, M = map(int, input().split())
A = [0] + list(map(int, input().split()))
dp = [[False] * 10001 for _ in range(N + 1)]
dp[0][0] = True

for i in range(1, N + 1):
    a = A[i]
    for j in range(10000):
        if j - a >= 0 and dp[i - 1][j - a]:
            dp[i][j] = True
        if dp[i - 1][j]:
            dp[i][j] = True
print("Yes" if dp[N][M] else "No")
