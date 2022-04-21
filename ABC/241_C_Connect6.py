N = int(input())
S = [input() for _ in range(N)]

for i in range(N):
    for j in range(N):
        row = 0
        column = 0
        rd = 0
        ru = 0
        for k in range(6):
            if j + 5 < N:
                if S[i][j + k] == "#":
                    row += 1
            if i + 5 < N:
                if S[i + k][j] == "#":
                    column += 1
            if i + 5 < N and j + 5 < N:
                if S[i + k][j + k] == "#":
                    rd += 1
            if i + 5 < N and j - 5 >= 0:
                if S[i + k][j - k] == "#":
                    ru += 1
        if row >= 4 or column >= 4 or rd >= 4 or ru >= 4:
            print("Yes")
            exit()
print("No")
