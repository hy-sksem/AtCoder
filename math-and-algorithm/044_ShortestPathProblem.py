import queue

N, M = map(int, input().split())
A = [None] * M
B = [None] * M
for i in range(M):
    A[i], B[i] = map(int, input().split())

G = [list() for i in range(N + 1)]
for i in range(M):
    G[A[i]].append(B[i])
    G[B[i]].append(A[i])

dist = [-1] * (N + 1)
dist[1] = 0

Q = queue.Queue()
Q.put(1)
while not Q.empty():
    u = Q.get()
    for v in G[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            Q.put(v)
for i in range(1, N + 1):
    print(dist[i])
