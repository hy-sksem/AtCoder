from collections import defaultdict

N, M = map(int, input().split())
d = defaultdict(list)

for i in range(M):
    A, B = map(int, input().split())
    d[A].append(B)

for i in range(N):
    print(*sorted(d[i]))
