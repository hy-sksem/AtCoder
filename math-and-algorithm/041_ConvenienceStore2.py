T = int(input())
N = int(input())
B = [0 for i in range(T + 2)]
A = [0 for i in range(T + 2)]

for i in range(N):
    a, b = map(int, input().split())
    B[a] += 1
    B[b] -= 1

A[0] = B[0]
for i in range(1, T):
    A[i] = A[i - 1] + B[i]

for i in range(T):
    print(A[i])
