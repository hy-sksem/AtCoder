from bisect import bisect_left

N, Q = map(int, input().split())
A = sorted(list(map(int, input().split())))

sum_a = [0] * (N + 1)
for i in range(N):
    sum_a[i + 1] = sum_a[i] + A[i]

for i in range(Q):
    x = int(input())
    idx = bisect_left(A, x)
    print(x * idx - sum_a[idx] + sum_a[N] - sum_a[idx] - x * (N - idx))
