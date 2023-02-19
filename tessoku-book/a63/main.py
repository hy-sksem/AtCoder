from collections import deque


N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

dist = [-1] * N
dist[0] = 0
q = deque()
q.append(0)
while q:
    v = q.popleft()
    for nv in G[v]:
        if dist[nv] != -1:
            continue
        dist[nv] = dist[v] + 1
        q.append(nv)

for i in range(N):
    print(dist[i])
