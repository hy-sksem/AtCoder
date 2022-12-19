N, M = map(int, input().split())
S = [input() for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(i + 1, N):
        flag = True
        for p, q in zip(S[i], S[j]):
            if p == "o" or q == "o":
                continue
            flag = False
        if flag:
            cnt += 1
print(cnt)
