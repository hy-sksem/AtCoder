H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

for i in range(H):
    for j in range(W - 1):
        if S[i][j] == S[i][j + 1] == "T":
            S[i][j], S[i][j + 1] = "P", "C"
for i in range(H):
    print("".join(S[i]))
