H, W, N = map(int, input().split())

S = [[0] * (W + 1) for _ in range(H + 1)]
Z = [[0] * (W + 1) for _ in range(H + 1)]

for _ in range(N):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    S[a][b] += 1
    S[a][d] -= 1
    S[c][b] -= 1
    S[c][d] += 1

# 横方向の累積和
for i in range(H + 1):
    for j in range(W + 1):
        Z[i][j] = Z[i][j - 1] + S[i][j]

# 縦方向の累積和
for j in range(W + 1):
    for i in range(1, H + 1):
        Z[i][j] = Z[i - 1][j] + Z[i][j]

for i in range(H):
    print(*Z[i][:-1])
