m = int(input())
M = [tuple(map(int, input().split())) for _ in range(m)]
n = int(input())
p = set([tuple(map(int, input().split())) for _ in range(n)])

for x, y in p:
    dx, dy = x - M[0][0], y - M[0][1]
    for mx, my in M:
        if not (mx + dx, my + dy) in p:
            break
    else:
        print(dx, dy)
