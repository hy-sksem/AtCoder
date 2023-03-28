import sys

sys.setrecursionlimit(1000000)


def dfs(pos, G, visited):
    visited[pos] = True
    path.append(pos)
    if pos == N:
        exit(print(*path))
    for i in G[pos]:
        if visited[i] is False:
            dfs(i, G, visited)
    path.pop()


N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

G = [[] for _ in range(N + 1)]
for a, b in edges:
    G[a].append(b)
    G[b].append(a)

visited = [False] * (N + 1)
path = []
dfs(1, G, visited)
