N, L, R = map(int, input().split())
A = list(map(int, input().split()))
dp_l = [0] * (N + 1)
dp_r = [0] * (N + 1)
for i in range(1, N + 1):
    dp_l[i] = min(dp_l[i - 1] + A[i - 1], L * i)
A = A[::-1]
for i in range(1, N + 1):
    dp_r[i] = min(dp_r[i - 1] + A[i - 1], R * i)

ans = sum(A)
for i in range(0, N + 1):
    ans = min(ans, dp_l[i] + dp_r[N - i])
print(ans)
