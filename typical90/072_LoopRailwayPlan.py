def dfs(sx, sy, px, py):
    if sx == px and sy == py and used[px][py]:
        return 0
    used[px][py] = True
    ret = -10000
    for i in range(4):
        nx, ny = px + dx[i], py + dy[i]
        if nx < 0 or ny < 0 or nx >= H or ny >= W or C[nx][ny] == "#":
            continue
        if (sx != nx or sy != ny) and used[nx][ny]:
            continue
        v = dfs(sx, sy, nx, ny)
        ret = max(ret, v + 1)
    used[px][py] = False
    return ret


H, W = map(int, input().split())
C = [input() for _ in range(H)]
dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)
used = [[False] * W for _ in range(H)]
ans = -1
for i in range(H):
    for j in range(W):
        ans = max(ans, dfs(i, j, i, j))

if ans <= 2:
    ans = -1
print(ans)
