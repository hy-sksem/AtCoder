H, W = map(int, input().split())
tgt = []
for i in range(H):
    for j, s in enumerate(input()):
        if s == "o":
            tgt.append((i, j))

print(abs(tgt[0][0] - tgt[1][0]) + abs(tgt[0][1] - tgt[1][1]))
