N = int(input())
A = list(map(int, input().split()))
D = int(input())
SL = [0] * N
SR = [0] * N

SL[0] = A[0]
SR[N - 1] = A[N - 1]
for i in range(1, N):
    SL[i] = max(A[i], SL[i - 1])
for i in range(N - 2, -1, -1):
    SR[i] = max(A[i], SR[i + 1])

for _ in range(D):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    print(max(SL[l - 1], SR[r + 1]))
