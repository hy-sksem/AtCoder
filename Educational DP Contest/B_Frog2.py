N, K = map(int, input().split())
H = list(map(int, input().split()))

c = [float("inf")] * N
c[0] = 0
for i in range(N):
    for j in range(1, K+1):
        if i+j < N:
            c[i+j] = min(c[i+j], c[i] + abs(H[i]-H[i+j]))

print(c[-1])
