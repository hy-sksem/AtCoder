N = int(input())
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())

A.sort()
B.sort()
ans = 10**18
for i in range(N // 2 - 1, N // 2 + 1):
    for j in range(N // 2 - 1, N // 2 + 1):
        s = A[i]
        g = B[j]
        tmp = 0
        for a, b in zip(A, B):
            tmp += abs(s - a)
            tmp += b - a
            tmp += abs(b - g)
        ans = min(ans, tmp)
print(ans)
