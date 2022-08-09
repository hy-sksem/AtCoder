N, M = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]

crr_mod = (B[0][0] + 6) % 7
for i in range(M):
    for j in range(1, N):
        if B[j][i] - B[j - 1][i] == 7:
            continue
        else:
            print("No")
            exit()
    if i > 0:
        if (B[0][i] + 6) % 7 - crr_mod == 1 and B[0][i] - B[0][i - 1] == 1:
            crr_mod = (B[0][i] + 6) % 7
            continue
        else:
            print("No")
            exit()
print("Yes")
