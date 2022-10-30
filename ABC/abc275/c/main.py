grid = []
pawn = set()
for i in range(1, 10):
    s = input()
    grid.append(s)
    for j in range(9):
        if s[j] == "#":
            pawn.add((i, j + 1))

ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        if (i, j) in pawn:
            for k in range(i, 10):
                for l in range(j + 1, 10):
                    if i == k and j == l:
                        continue
                    if (k, l) in pawn:
                        dx = l - j
                        dy = k - i
                        x1 = k + dx
                        y1 = l - dy
                        x2 = i + dx
                        y2 = j - dy
                        if (x1, y1) in pawn and (x2, y2) in pawn:
                            ans += 1
print(ans)
