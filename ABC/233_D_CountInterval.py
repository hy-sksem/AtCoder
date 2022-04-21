from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

d = defaultdict(lambda : 0)
d[0] = 1
s = 0
ans = 0

for a in A:
    s += a
    ans += d[s-K]
    d[s] += 1
print(ans)
