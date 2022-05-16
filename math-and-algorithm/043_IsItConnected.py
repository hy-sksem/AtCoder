import sys


def DFS(pos):
    visited[pos] = True
    for i in G[pos]:
        if not visited[i]:
            DFS(i)


sys.setrecursionlimit(120000)

N, M = map(int, input().split())
A = [None] * M
B = [None] * M
for i in range(M):
    A[i], B[i] = map(int, input().split())

G = [list() for i in range(N + 1)]
for i in range(M):
    G[A[i]].append(B[i])
    G[B[i]].append(A[i])
visited = [False] * (N + 1)
DFS(1)

ans = True
for i in range(1, N + 1):
    if not visited[i]:
        ans = False
        break
print("The graph is connected." if ans else "The graph is not connected.")
