H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

row = [0] * H
col = [0] * W

for i in range(H):
    for j in range(W):
        row[i] += A[i][j]
        col[j] += A[i][j]

for i in range(H):
    ans = []
    for j in range(W):
        ans.append(row[i] + col[j] - A[i][j])
    print(*ans)
