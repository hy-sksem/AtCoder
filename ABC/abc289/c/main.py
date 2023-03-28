N, M = map(int, input().split())
A = []
for i in range(M):
    c = int(input())
    a = set(map(int, input().split()))
    A.append(a)

comp = set(range(1, N + 1))
cnt = 0
for i in range(1, 1 << M):
    tmp = set()
    for j in range(M):
        if (i >> j) & 1:
            tmp |= A[j]
    if tmp == comp:
        cnt += 1
print(cnt)
