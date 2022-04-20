import heapq


def dijkstra(path, s):
    n = len(path)
    node = [float("INF")] * n
    node[s] = 0
    q = [(0, s)]
    seen = [False] * n
    while q:
        c, v = heapq.heappop(q)
        if node[v] >= c:
            seen[v] = True
            for i, j in path[v]:
                if seen[i] == False and node[v] + j < node[i]:
                    node[i] = c + j
                    heapq.heappush(q, (node[i], i))
    return node


N, M = map(int, input().split())
path = [[] for i in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    path[a-1] += [[b-1, c]]
    path[b-1] += [[a-1, c]]

d1 = dijkstra(path, 0)
d2 = dijkstra(path, N-1)

for i in range(N):
    print(d1[i] + d2[i])
