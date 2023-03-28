N, M, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [10**18] * (M + 1)
dp[0] = 0

for i in range(N):
    a = A[i]
    for j in range(M, -1, -1):
        if j - a >= 0:
            dp[j] = min(dp[j], dp[j - a] + 1)
print("Yes" if dp[M] <= K else "No")

# 2重ループ
# dp = [[10**18] * (M + 1) for _ in range(N + 1)]
# dp[0][0] = 0

# for i in range(N):
#     a = A[i]
#     for j in range(M + 1):
#         if j - a >= 0:
#             dp[i + 1][j] = min(dp[i + 1][j], dp[i][j - a] + 1)
#         dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
# print("Yes" if dp[N][M] <= K else "No")
