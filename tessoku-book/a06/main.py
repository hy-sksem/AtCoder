N, Q = map(int, input().split())
A = list(map(int, input().split()))
s = [0] * (N + 1)
for i in range(1, N + 1):
    s[i] = s[i - 1] + A[i - 1]

for i in range(Q):
    l, r = map(int, input().split())
    print(s[r] - s[l - 1])
