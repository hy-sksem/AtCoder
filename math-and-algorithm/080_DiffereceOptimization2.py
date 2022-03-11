import heapq

N, M = map(int, input().split())
A, B, C = [None] * M, [None] * M, [None] * M
for i in range(M):
    A[i], B[i], C[i] = map(int, input().split())

G = [list() for i in range(N + 1)]
for i in range(M):
    G[A[i]].append((B[i], C[i]))
    G[B[i]].append((A[i], C[i]))

dist = [10**19] * (N + 1)
used = [False] * (N + 1)
Q = list()
dist[1] = 0
heapq.heappush(Q, (0, 1))

while len(Q) >= 1:
    pos = heapq.heappop(Q)[1]
    if used[pos]:
        continue
    used[pos] = True
    for i in G[pos]:
        if dist[i[0]] > dist[pos] + i[1]:
            dist[i[0]] = dist[pos] + i[1]
            heapq.heappush(Q, (dist[i[0]], i[0]))

if dist[N] != 10**19:
    print(dist[N])
else:
    print(-1)
