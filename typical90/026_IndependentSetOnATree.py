from collections import deque

N = int(input())
G = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

dist = [-1] * N
dist[0] = 0
q = deque([0])
while q:
    now = q.popleft()
    for nex in G[now]:
        if dist[nex] == -1:
            dist[nex] = dist[now] + 1
            q.append(nex)

X = [[], []]
for i in range(N):
    X[dist[i] % 2].append(1 + i)
Y = X[0] if len(X[0]) > len(X[1]) else X[1]
print(*Y[: N // 2])
