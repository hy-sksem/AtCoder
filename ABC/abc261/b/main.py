N = int(input())
A = [input() for _ in range(N)]

for i in range(N):
    for j in range(i, N):
        if i == j:
            continue
        if A[i][j] == A[j][i] == "D":
            continue
        elif (A[i][j] == "W" and A[j][i] == "L") or (A[i][j] == "L" and A[j][i] == "W"):
            continue
        else:
            print("incorrect")
            exit()
print("correct")
