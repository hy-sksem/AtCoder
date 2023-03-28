# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cg

N = int(input())
grid = [[0] * 1505 for _ in range(1505)]
for i in range(N):
    x, y = map(int, input().split())
    grid[x][y] += 1

# 横方向の累積和
s = [[0] * 1505 for _ in range(1505)]
for h in range(1505):
    for w in range(1505):
        s[h][w] = s[h][w - 1] + grid[h][w]

# 縦方向の累積和
for w in range(1505):
    for h in range(1, 1505):
        s[h][w] = s[h - 1][w] + s[h][w]

for i in range(int(input())):
    a, b, c, d = map(int, input().split())
    print(s[c][d] + s[a - 1][b - 1] - s[c][b - 1] - s[a - 1][d])
