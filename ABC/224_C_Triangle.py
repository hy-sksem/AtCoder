N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            a, b = XY[i]
            c, d = XY[j]
            e, f = XY[k]
            if (a - c) * (d - f) == (b - d) * (c - e):
                cnt += 1

print(N * (N - 1) * (N - 2) // 6 - cnt)
