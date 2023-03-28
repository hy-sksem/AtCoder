N = int(input())
A = [0] + list(map(int, input().split()))
B = [0] * 2 + list(map(int, input().split()))

dp = [10**18] * (N)
dp[0] = 0
dp[1] = A[1]
for i in range(2, N):
    dp[i] = min(dp[i - 1] + A[i], dp[i - 2] + B[i])
print(dp[N - 1])
