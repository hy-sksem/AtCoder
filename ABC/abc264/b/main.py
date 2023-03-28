R, C = map(int, input().split())

grid = [["black"] * 15 for _ in range(15)]

c = "white"
cnt = 1
while cnt < 14:
    for i in range(cnt, 15 - cnt):
        for j in range(cnt, 15 - cnt):
            grid[i][j] = c
    cnt += 1
    c = "white" if c == "black" else "black"
print(grid[R - 1][C - 1])
