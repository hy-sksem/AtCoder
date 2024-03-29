from copy import copy

H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]

h = set()
p = (0, 0)


def can_move(i, j):
    _i, _j = copy(p)
    return 0 <= (i + _i) <= H - 1 and 0 <= (j + _j) <= W - 1


while True:
    i, j = p
    if grid[i][j] == "U":
        tmp = (-1, 0)
    elif grid[i][j] == "D":
        tmp = (1, 0)
    elif grid[i][j] == "L":
        tmp = (0, -1)
    elif grid[i][j] == "R":
        tmp = (0, 1)
    if not can_move(*tmp):
        print(i + 1, j + 1)
        exit()
    p = (i + tmp[0], j + tmp[1])
    if p in h:
        print(-1)
        exit()
    h.add(p)
