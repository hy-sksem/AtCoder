N = 8
S = [input() for _ in range(N)]


for i in range(N):
    for j in range(N):
        if S[i][j] == "*":
            first = chr(j + ord("a"))
            second = str(N - i)
            exit(print(first + second))
