def int1(x: int) -> int:
    return int(x) - 1


def dfs(pos, prev):
    A = 1
    AB = 0
    for p in G[pos]:
        if p == prev:
            continue
        a, ab = dfs(p, pos)
        if C[p] == C[pos]:
            AB = AB * (a + ab + ab) + A * ab
            A *= ab + a
        else:
            AB = AB * (a + ab + ab) + A * (a + ab)
            A *= ab
        AB %= mod
        A %= mod
    return A, AB


N = int(input())
C = input().split()
G = [[] for _ in range(N)]
mod = 10**9 + 7

for i in range(N - 1):
    _a, _b = map(int1, input().split())
    G[_a].append(_b)
    G[_b].append(_a)
_, ans = dfs(0, 0)
print(ans)
