def check(x, y):
    if 0 <= x < R and 0 <= y < C:
        if B[x][y] == "#":
            B[x][y] = "."


def bomb(x, y, dist):
    for i in range(R):
        for j in range(C):
            if abs(x - i) + abs(y - j) <= dist:
                check(i, j)


R, C = map(int, input().split())
B = [list(input()) for _ in range(R)]
for i in range(R):
    for j in range(C):
        try:
            dist = int(B[i][j])
            bomb(i, j, dist)
            B[i][j] = "."
        except ValueError:
            continue

for i in range(R):
    print("".join(B[i]))
