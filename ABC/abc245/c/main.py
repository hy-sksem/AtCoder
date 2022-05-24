N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.insert(0, 0)
B.insert(0, 0)

dp = [False] * (N + 1)
ep = [False] * (N + 1)
dp[1] = ep[1] = True

for i in range(2, N + 1):
    if dp[i - 1]:
        if abs(A[i - 1] - A[i]) <= K:
            dp[i] = True
        if abs(A[i - 1] - B[i]) <= K:
            ep[i] = True
    if ep[i - 1]:
        if abs(B[i - 1] - A[i]) <= K:
            dp[i] = True
        if abs(B[i - 1] - B[i]) <= K:
            ep[i] = True
if dp[N] or ep[N]:
    print("Yes")
else:
    print("No")
