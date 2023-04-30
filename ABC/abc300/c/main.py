H, W = map(int, input().split())
C = [input() for _ in range(H)]

S = [0 for _ in range(min(H, W))]

for i in range(1, H - 1):
    for j in range(1, W - 1):
        c = C[i][j]
        lu = C[i - 1][j - 1]
        ru = C[i - 1][j + 1]
        ld = C[i + 1][j - 1]
        rd = C[i + 1][j + 1]
        if c == lu == ru == ld == rd == "#":
            cnt = 0
            h, w = i, j
            while True:
                h += 1
                w += 1
                if h < H and w < W and C[h][w] == "#":
                    cnt += 1
                else:
                    break
            S[cnt - 1] += 1
print(*S)
