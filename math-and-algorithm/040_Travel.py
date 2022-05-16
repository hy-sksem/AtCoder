N = int(input())
A = list(map(int, input().split()))
A.insert(0, 0)
M = int(input())
B = [int(input()) for _ in range(M)]
B.insert(0, 0)

S = [0] * (N + 2)
S[1] = 0
for i in range(2, N + 1):
    S[i] = S[i - 1] + A[i - 1]
ans = 0
for i in range(1, M):
    if B[i] < B[i + 1]:
        ans += S[B[i + 1]] - S[B[i]]
    else:
        ans += S[B[i]] - S[B[i + 1]]
print(ans)
