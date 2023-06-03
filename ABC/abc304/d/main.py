from collections import defaultdict
from bisect import bisect_left

W, H = map(int, input().split())
N = int(input())
pq = [list(map(int, input().split())) for _ in range(N)]
A = int(input())
a = list(map(int, input().split()))
B = int(input())
b = list(map(int, input().split()))

d = defaultdict(int)

for i in range(N):
    p, q = pq[i]
    x = bisect_left(a, p)
    y = bisect_left(b, q)
    d[(x, y)] += 1

mini = 10**9
maxi = 0
for v in d.values():
    mini = min(mini, v)
    maxi = max(maxi, v)
if len(d) == (A + 1) * (B + 1):
    print(mini, maxi)
else:
    print(0, maxi)
