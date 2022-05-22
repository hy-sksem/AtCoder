import math
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

d = defaultdict(int)

for i in range(N):
    d[A[i]] += 1

ans = math.comb(N, 3)
for k, v in d.items():
    if v == 1:
        continue
    if v == 2:
        ans -= N - 2
    else:
        dup = math.comb(N - v, 1) * math.comb(v, 2) + math.comb(v, 3)
        ans -= dup
print(int(ans))
