from collections import defaultdict

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]

ans = defaultdict(int)

for i in range(1, N + 1):
    ans[i] = set(range(1, N + 1))
    ans[i].remove(i)
for i in range(M):
    for j in range(N - 1):
        x1 = A[i][j]
        x2 = A[i][j + 1]
        if x2 in ans[x1]:
            ans[x1].remove(x2)
        if x1 in ans[x2]:
            ans[x2].remove(x1)

cnt = 0
for i in range(1, N + 1):
    cnt += len(ans[i])
print(cnt // 2)
