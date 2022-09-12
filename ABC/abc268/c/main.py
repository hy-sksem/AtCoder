N = int(input())
P = list(map(int, input().split()))

A = [0] * N

for i, p in enumerate(P):
    A[(i - p - 1) % N] += 1
    A[(i - p) % N] += 1
    A[(i - p + 1) % N] += 1

print(max(A))
