N = int(input())
S = list(input())

for i in range(1, N):
    cnt = 0
    for j in range(N - 1):
        if j + i >= N:
            break
        if S[j] != S[j + i]:
            cnt += 1
        else:
            break
    print(cnt)
