N = int(input())
lx = [0] * (N + 1)
ly = [0] * (N + 1)
rx = [0] * (N + 1)
ry = [0] * (N + 1)
for i in range(1, N + 1):
    lx[i], ly[i], rx[i], ry[i] = map(int, input().split())

xy = [[0] * (1002) for i in range(1002)]

# いもす法による重みの加算
for i in range(1, N + 1):
    xy[lx[i]][ly[i]] += 1
    xy[lx[i]][ry[i]] -= 1
    xy[rx[i]][ly[i]] -= 1
    xy[rx[i]][ry[i]] += 1

# 横方向への累積和
for i in range(1001):
    for j in range(1, 1001):
        xy[i][j] += xy[i][j - 1]

# 縦方向への累積和
for i in range(1, 1001):
    for j in range(1001):
        xy[i][j] += xy[i - 1][j]

# シミュレート
ans = [0] * (N + 1)
for i in range(1001):
    for j in range(1001):
        if xy[i][j] > 0:
            ans[xy[i][j]] += 1

for i in range(1, N + 1):
    print(ans[i])
