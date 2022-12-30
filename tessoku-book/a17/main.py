N = int(input())
A = [0] + list(map(int, input().split()))
B = [0] * 2 + list(map(int, input().split()))

dp = [10**18] * N
dp[0] = 0
dp[1] = A[1]

for i in range(2, N):
    dp[i] = min(dp[i - 1] + A[i], dp[i - 2] + B[i])

ans = [N]
idx = N - 1
while idx > 0:
    if dp[idx - 1] + A[idx] == dp[idx]:
        ans.append(idx)
        idx -= 1
    else:
        ans.append(idx - 1)
        idx -= 2
print(len(ans))
print(*ans[::-1])
