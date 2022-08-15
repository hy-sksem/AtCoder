N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for j in range(M):
    for jj in range(j + 1, M):
        cnt = 0
        for i in range(N):
            cnt += max(A[i][j], A[i][jj])
        ans = max(ans, cnt)
print(ans)
