from collections import defaultdict

N, M = map(int, input().split())
if M == 0:
    exit()
d = defaultdict(list)

for i in range(M):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)

f = defaultdict(list)
cnt = 0
for k, v in d.items():
    f[len(v)].append(k)
    cnt = max(cnt, len(v))

print(*sorted(d[sorted(f[cnt])[0]]))
