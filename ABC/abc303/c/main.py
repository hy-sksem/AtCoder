def move(x, y, H):
    H -= 1
    if H < 0:
        exit(print("No"))
    if (x, y) in xy and H < K:
        H = K
        xy.remove((x, y))
    return x, y, H


N, M, H, K = map(int, input().split())
S = input()
xy = set([tuple(map(int, input().split())) for _ in range(M)])


pos = (0, 0)
for s in S:
    # print(pos, H)
    if s == "U":
        *pos, H = move(pos[0], pos[1] + 1, H)
    elif s == "D":
        *pos, H = move(pos[0], pos[1] - 1, H)
    elif s == "L":
        *pos, H = move(pos[0] - 1, pos[1], H)
    elif s == "R":
        *pos, H = move(pos[0] + 1, pos[1], H)
print("Yes")
