from collections import defaultdict


N = int(input())
A = [0] * 2 + list(map(int, input().split()))

d = defaultdict(list)
for i in range(2, N + 1):
    d[A[i]].append(i)

ans = [0] * (N + 1)
for i in range(N, 0, -1):
    for j in d[i]:
        ans[i] += ans[j] + 1
print(*ans[1:])
