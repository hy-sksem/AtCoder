import bisect

N = int(input())
A = list(map(int, input().split()))
l = [0] * N
r = [0] * N

p = []
for i in range(N):
    idx = bisect.bisect_left(p, A[i])
    if idx < len(p):
        p[idx] = A[i]
    else:
        p.append(A[i])
    l[i] = idx

q = []
for i in range(N - 1, -1, -1):
    idx = bisect.bisect_left(q, A[i])
    if idx < len(q):
        q[idx] = A[i]
    else:
        q.append(A[i])
    r[i] = idx

ans = 0
for i in range(N):
    ans = max(ans, l[i] + r[i] + 1)
print(ans)
