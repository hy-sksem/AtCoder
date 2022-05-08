from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

d = defaultdict(int)
ans = 0
cnt = 0
l, r = 0, 0

for l in range(N):
    while r < N:
        if d[A[r]] == 0 and cnt == K:
            break
        if d[A[r]] == 0:
            cnt += 1
        d[A[r]] += 1
        r += 1
    ans = max(ans, r - l)
    if d[A[l]] == 1:
        cnt -= 1
    d[A[l]] -= 1
print(ans)
