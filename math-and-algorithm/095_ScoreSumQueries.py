N = int(input())
C = [None] * (N + 1)
P = [None] * (N + 1)
for i in range(1, N + 1):
    C[i], P[i] = map(int, input().split())

S1 = [None] * (N + 1)
S1[0] = 0
for i in range(1, N + 1):
    S1[i] = S1[i - 1] + (P[i] if C[i] == 1 else 0)
S2 = [None] * (N + 1)
S2[0] = 0
for i in range(1, N + 1):
    S2[i] = S2[i - 1] + (P[i] if C[i] == 2 else 0)

Q = int(input())
ans = []
for i in range(Q):
    L, R = map(int, input().split())
    ans.append([S1[R] - S1[L - 1], S2[R] - S2[L - 1]])

for i in range(Q):
    print(*ans[i])
