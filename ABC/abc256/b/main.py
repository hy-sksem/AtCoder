def hit(x):
    P.append(1)
    for i in range(x - 1):
        P.append(0)


N = int(input())
A = list(map(int, input().split()))
P = []

for i in range(N):
    hit(A[i])
print(sum(P) - sum(P[-3:]))
