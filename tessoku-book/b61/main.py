from collections import defaultdict

N, M = map(int, input().split())
d = defaultdict(list)
for i in range(M):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)

cnt = 0
ans = 0
for k, v in d.items():
    if len(v) >= cnt:
        cnt = len(v)
        ans = k
print(ans)
