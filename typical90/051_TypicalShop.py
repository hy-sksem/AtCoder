import bisect
from itertools import combinations

N, K, P = map(int, input().split())
A = list(map(int, input().split()))

left, right = A[: N // 2], A[N // 2 :]
left_p = [[] for _ in range(K + 1)]

for i in range(K + 1):
    for c in combinations(left, i):
        left_p[i].append(sum(c))
    left_p[i].sort()

ans = 0
for i in range(K + 1):
    for c in combinations(right, i):
        index = bisect.bisect_right(left_p[K - i], P - sum(c))
        ans += index
print(ans)
