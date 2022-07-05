N = int(input())
A = [list(input()) for i in range(N)]

m = 0
for i in range(N):
    for j in range(N):
        m = max(m, int(A[i][j]))

for i in range(N):
    A[i] *= 3
A *= 3

comb = [-1, 0, 1]
ans = 0
for i in range(N, N + N):
    for j in range(N, N + N):
        if int(A[i][j]) == m:
            for k in comb:
                for l in comb:
                    temp = int(A[i][j])
                    if k == l == 0:
                        continue
                    for x in range(1, N):
                        temp *= 10
                        temp += int(A[i + k * x][j + l * x])
                    ans = max(ans, temp)
print(ans)
