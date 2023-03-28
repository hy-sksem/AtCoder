N = int(input())

S = [[0] * 1501 for _ in range(1501)]
X = [[0] * 1501 for _ in range(1501)]

for _ in range(N):
    a, b, c, d = map(int, input().split())
    S[a][b] += 1
    S[a][d] -= 1
    S[c][b] -= 1
    S[c][d] += 1

for h in range(1501):
    for w in range(1501):
        if w == 0:
            X[h][w] = S[h][w]
            continue
        X[h][w] = X[h][w - 1] + S[h][w]

for w in range(1501):
    for h in range(1501):
        if h == 0:
            continue
        X[h][w] = X[h - 1][w] + X[h][w]

ans = 0
for h in range(1500):
    for w in range(1500):
        if X[h][w] >= 1:
            ans += 1

print(ans)
