N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i, j in enumerate(xy):
    for k, l in enumerate(xy):
        if k <= i:
            continue
        else:
            t = (l[1] - j[1]) / (l[0] - j[0])
            ans += 1 if t >= -1 and t <= 1 else 0

print(ans)
