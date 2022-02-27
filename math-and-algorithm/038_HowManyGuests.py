N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.insert(0, 0)
B = [0] * (N+1)
for i in range(1, N+1):
    B[i] = B[i-1] + A[i]
ans = []
for i in range(Q):
    L, R = map(int, input().split())
    ans.append(B[R] - B[L-1])
print(*ans, sep='\n')
