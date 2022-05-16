import sys


def DFS(pos, G, color):
    for i in G[pos]:
        if color[i] == 0:
            color[i] = 3 - color[pos]
            DFS(i, G, color)


sys.setrecursionlimit(210000)

N, M = map(int, input().split())
A = [None] * M
B = [None] * M
for i in range(M):
    A[i], B[i] = map(int, input().split())

# 隣接リスト
G = [list() for i in range(N + 1)]
for i in range(M):
    G[A[i]].append(B[i])
    G[B[i]].append(A[i])

# 深さ優先探索
color = [0] * (N + 1)
for i in range(1, N + 1):
    if color[i] == 0:
        color[i] = 1
        DFS(i, G, color)

ans = True
for i in range(M):
    if color[A[i]] == color[B[i]]:
        ans = False
        break
print("Yes" if ans else "No")
