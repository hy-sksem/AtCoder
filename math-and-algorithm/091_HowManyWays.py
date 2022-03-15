N, X = map(int, input().split())

cnt = 0
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        for k in range(j + 1, N + 1):
            if i + j + k == X:
                cnt += 1
print(cnt)
