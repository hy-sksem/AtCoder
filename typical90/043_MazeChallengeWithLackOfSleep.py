from collections import deque


def int1(x: int) -> int:
    return int(x) - 1


H, W = map(int, input().split())
rs, cs = map(int1, input().split())
rt, ct = map(int1, input().split())
grid = [input() for i in range(H)]

INF = 10**9
dp = [[INF for _ in range(W)] for _ in range(H)]
dp[rs][cs] = -1  # start
d = ((0, 1), (-1, 0), (0, -1), (1, 0))
q = deque()
q.append(((rs, cs)))
while q:
    r, c = q.popleft()
    t = dp[r][c]
    for dr, dc in d:
        rn = r + dr
        cn = c + dc
        while (
            0 <= rn < H and 0 <= cn < W and grid[rn][cn] == "." and t + 1 <= dp[rn][cn]
        ):
            if dp[rn][cn] == INF:
                q.append((rn, cn))
            dp[rn][cn] = t + 1
            rn += dr
            cn += dc
print(dp[rt][ct])
