H, W = map(int, input().split())
X = [[0] * (W + 1)] + [[0] + list(map(int, input().split())) for _ in range(H)]
S = [[0] * (W + 1) for _ in range(H + 1)]

# 横方向の累積和
for i in range(H + 1):
    for j in range(W + 1):
        S[i][j] = S[i][j - 1] + X[i][j]

# 縦方向の累積和
for j in range(W + 1):
    for i in range(1, H + 1):
        S[i][j] = S[i - 1][j] + S[i][j]

for i in range(int(input())):
    a, b, c, d = map(int, input().split())
    print(S[c][d] + S[a - 1][b - 1] - S[c][b - 1] - S[a - 1][d])
