import sys

sys.setrecursionlimit(1 << 30)


def int1(x: int) -> int:
    return int(x) - 1


def dfs(parent: int, i: int):
    for j in g[i]:
        if j == parent:
            continue
        r = dfs(i, j) + 1
        if r > rank[i]:
            rank[i] = r
    return rank[i]


N, T = map(int, input().split())
T -= 1
g = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int1, input().split())
    g[a].append(b)
    g[b].append(a)

rank = [0] * N
dfs(-1, T)
print(*rank)
