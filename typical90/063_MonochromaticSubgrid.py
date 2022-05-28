from collections import defaultdict

H, W = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]

ans = 0
for h in range(1, 1 << H):
    row = []
    for i in range(H):
        if h >> i & 1:
            row.append(i)
    cnt = defaultdict(int)
    for j in range(W):
        flag = True
        b = -1
        for i in row:
            # print("i, j, grid[i][j]", i, j, grid[i][j])
            if b == -1:
                b = grid[i][j]
            elif b != grid[i][j]:
                flag = False
                break
        if flag:
            cnt[b] += len(row)
    if cnt:
        ans = max(ans, max(cnt.values()))
print(ans)
