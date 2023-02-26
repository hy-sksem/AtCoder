import heapq


N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
    G[b].append((a, c))

# ダイクストラ法
INF = 10**18
conf = [False] * (N + 1)
cur = [INF] * (N + 1)
cur[1] = 0
q = []
heapq.heappush(q, (0, 1))
while q:
    pos = heapq.heappop(q)[1]
    if conf[pos]:
        continue
    conf[pos] = True
    for nex, cost in G[pos]:
        if cur[nex] > cur[pos] + cost:
            cur[nex] = cur[pos] + cost
            heapq.heappush(q, (cur[nex], nex))

for i in range(1, N + 1):
    print(cur[i] if cur[i] != INF else -1)
