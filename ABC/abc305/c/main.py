def check(tgt, h, w, S):
    cnt = 0
    for t in tgt:
        if t == "u" and S[h - 1][w] == "#":
            cnt += 1
        elif t == "d" and S[h + 1][w] == "#":
            cnt += 1
        elif t == "l" and S[h][w - 1] == "#":
            cnt += 1
        elif t == "r" and S[h][w + 1] == "#":
            cnt += 1
    return cnt


H, W = map(int, input().split())
S = [input() for _ in range(H)]

for h in range(H):
    for w in range(W):
        if S[h][w] == "#":
            continue
        tgt = []
        if h >= 0:
            tgt.append("u")
        if h < H - 1:
            tgt.append("d")
        if w >= 0:
            tgt.append("l")
        if w < W - 1:
            tgt.append("r")
        if check(tgt, h, w, S) >= 2:
            exit(print(h + 1, w + 1))
