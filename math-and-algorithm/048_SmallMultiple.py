import heapq

K = int(input())

G = [list() for _ in range(K)]
for i in range(K):
    for j in range(10):
        if i == 0 and j == 0:
            continue
        G[i].append(((i * 10 + j) % K, j))

dist = [10 ** 10] * K
used = [False] * K
Q = list()
heapq.heappush(Q, (0, 0))

while len(Q) > 0:
    u = heapq.heappop(Q)
    if used[u[1]]:
        continue
    used[u[1]] = True
    for v in G[u[1]]:
        if dist[v[0]] > u[0] + v[1]:
            dist[v[0]] = u[0] + v[1]
            heapq.heappush(Q, (dist[v[0]], v[0]))
print(dist[0])
