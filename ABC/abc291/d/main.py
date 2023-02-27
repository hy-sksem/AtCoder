N = int(input())
AB = [None] * N
for i in range(N):
    AB[i] = tuple(map(int, input().split()))

MOD = 998_244_353
A, B = [0] * (N + 1), [0] * (N + 1)
A[0], B[0] = 1, 1
for i in range(1, N):
    a, b = AB[i]
    prev_a, prev_b = AB[i - 1]
    tmp_a, tmp_b = 0, 0
    if a != prev_a:
        tmp_a += A[i - 1]
    if a != prev_b:
        tmp_a += B[i - 1]
    if b != prev_a:
        tmp_b += A[i - 1]
    if b != prev_b:
        tmp_b += B[i - 1]
    A[i], B[i] = tmp_a % MOD, tmp_b % MOD

print((A[N - 1] + B[N - 1]) % MOD)
