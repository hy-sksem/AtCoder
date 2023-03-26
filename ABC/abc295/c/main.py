from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

d = defaultdict(int)
ans = 0
for i in range(N):
    a = A[i]
    d[a] += 1
    if d[a] % 2 == 0:
        ans += 1
        d[a] = 0
print(ans)
