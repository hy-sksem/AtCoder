N = int(input())
A = [0.0 for _ in range(N)]
B = [0.0 for _ in range(N)]
C = [0.0 for _ in range(N)]

for i in range(N):
    A[i], B[i], C[i] = map(float, input().split())

ans = 0.0
for i in range(N):
    for j in range(i + 1, N):
        if A[i] * B[j] == A[j] * B[i]:
            continue

        px = (C[i] * B[j] - C[j] * B[i]) / (A[i] * B[j] - A[j] * B[i])
        py = (C[i] * A[j] - C[j] * A[i]) / (B[i] * A[j] - B[j] * A[i])

        ret = True
        for k in range(N):
            if A[k] * px + B[k] * py > C[k]:
                ret = False
        if ret == True:
            ans = max(ans, px + py)

print("%.12f" % ans)
