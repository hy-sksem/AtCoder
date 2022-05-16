N, X = map(int, input().split())
dp = [[False] * (X + 2) for _ in range(N + 1)]
A = [None] * (N + 1)
B = [None] * (N + 1)

for i in range(1, N + 1):
    A[i], B[i] = map(int, input().split())

if A[1] <= X:
    dp[1][A[1]] = True
if B[1] <= X:
    dp[1][B[1]] = True

for i in range(2, N + 1):
    for j in range(1, X + 2):
        if dp[i - 1][j]:
            if j + A[i] <= X:
                dp[i][j + A[i]] = True
            if j + B[i] <= X:
                dp[i][j + B[i]] = True

print("Yes" if dp[N][X] else "No")
