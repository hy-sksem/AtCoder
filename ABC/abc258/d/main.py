N, X = map(int, input().split())
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())

ans = float("inf")
now = 0
for i in range(N):
    ans = min(ans, now + A[i] + B[i] * X)
    now += A[i] + B[i]
    X -= 1
    if X == 0:
        break
print(ans)
