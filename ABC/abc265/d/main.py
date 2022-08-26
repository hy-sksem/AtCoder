N, P, Q, R = map(int, input().split())
A = list(map(int, input().split()))
sum_a = [0] * (N + 1)
for i in range(N):
    sum_a[i + 1] = A[i] + sum_a[i]

s_sum_a = set(sum_a)
for i in range(N):
    x = sum_a[i]
    if x + P in s_sum_a and x + P + Q in s_sum_a and x + P + Q + R in s_sum_a:
        print("Yes")
        exit()
print("No")
