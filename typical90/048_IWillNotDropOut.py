N, K = map(int, input().split())
A = []
B = []

for i in range(N):
    a, b = map(int, input().split())
    A.append(a - b)
    B.append(b)
ab = sorted(A + B, reverse=True)
print(sum(ab[:K]))
