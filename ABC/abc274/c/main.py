from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
d = defaultdict(int)
d[1] = 0
for i, a in enumerate(A, start=1):
    d[2 * i] = d[a] + 1
    d[2 * i + 1] = d[a] + 1

for v in d.values():
    print(v)
