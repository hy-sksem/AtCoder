import math
from bisect import bisect_left

N, H = map(int, input().split())
a, b = [0] * N, [0] * N
for i in range(N):
    a[i], b[i] = map(int, input().split())

a.sort()
b.sort()
idx = bisect_left(b, a[-1])
cnt = 0
for i in range(N - 1, idx - 1, -1):
    H -= b[i]
    cnt += 1
    if H <= 0:
        break

if H > 0:
    cnt += math.ceil(H / a[-1])
print(cnt)
