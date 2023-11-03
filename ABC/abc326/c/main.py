N, M = map(int, input().split())
A = list(map(int, input().split()))

A = sorted(A)
A.append(10**18)

ans = 0
r = 0
for l in range(N):
    while A[r] < A[l] + M:
        r += 1
    ans = max(ans, r - l)
print(ans)
