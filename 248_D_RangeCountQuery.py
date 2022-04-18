from collections import defaultdict
import bisect

N = int(input())
A = list(map(int, input().split()))
indexes = defaultdict(list)
for i in range(N):
    indexes[A[i]].append(i)

for i in range(int(input())):
    l, r, x = map(int, input().split())
    l -= 1
    r -= 1
    l_index = bisect.bisect_left(indexes[x], l)
    r_index = bisect.bisect_right(indexes[x], r)
    print(r_index - l_index)
