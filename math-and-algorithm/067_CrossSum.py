H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

row = [0 for i in range(H)]
for i in range(H):
    for j in range(W):
        row[i] += A[i][j]

column = [0 for i in range(W)]
for i in range(W):
    for j in range(H):
        column[i] += A[j][i]

ans = [[0 for j in range(W)] for i in range(H)]
for i in range(H):
    for j in range(W):
        ans[i][j] = row[i] + column[j] - A[i][j]

for i in range(H):
    print(*ans[i])
