from collections import defaultdict

N, M = map(int, input().split())
G = defaultdict(list)

for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

ans = 0
for k, v in G.items():
    cnt = 0
    for i in v:
        if k > i:
            cnt += 1
    if cnt == 1:
        ans += 1
print(ans)
