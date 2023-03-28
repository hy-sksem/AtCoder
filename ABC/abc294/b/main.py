H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

ans = []
for i in range(H):
    row = ""
    for j in range(W):
        if A[i][j] == 0:
            row += "."
        else:
            row += chr(A[i][j] + ord("A") - 1)
    ans.append(row)

print(*ans, sep="\n")
