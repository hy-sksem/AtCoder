import sys

sys.setrecursionlimit(100000)


def dfs(pos, G, visited):
    visited[pos] = True
    for i in G[pos]:
        if visited[i] is False:
            dfs(i, G, visited)


N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

G = [[] for _ in range(N)]
for a, b in edges:
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

visited = [False] * N
dfs(0, G, visited)
ans = True
for i in range(N):
    if visited[i] is False:
        ans = False
        break

print("The graph is connected." if ans else "The graph is not connected.")
