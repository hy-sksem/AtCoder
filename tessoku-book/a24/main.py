from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))

length = 0
L = []
dp = [None] * N

for i in range(N):
    pos = bisect_left(L, A[i])
    dp[i] = pos
    if dp[i] >= length:
        L.append(A[i])
        length += 1
    else:
        L[dp[i]] = A[i]
print(length)
