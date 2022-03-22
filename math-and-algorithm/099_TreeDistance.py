import sys


def DFS(pos, G, visited, dp):
    visited[pos] = True
    dp[pos] = 1
    for i in G[pos]:
        if not visited[i]:
            DFS(i, G, visited, dp)
            dp[pos] += dp[i]


sys.setrecursionlimit(120000)

N = int(input())
A = [None] * (N - 1)
B = [None] * (N - 1)
for i in range(N - 1):
    A[i], B[i] = map(int, input().split())

G = [list() for _ in range(N + 1)]
for i in range(N - 1):
    G[A[i]].append(B[i])
    G[B[i]].append(A[i])

visited = [False] * (N + 1)
dp = [None] * (N + 1)
DFS(1, G, visited, dp)

ans = 0
for i in range(2, N + 1):
    ans += dp[i] * (N - dp[i])
print(ans)
