N = int(input())
H = list(map(int, input().split()))

F = [100000] * (N)
F[0] = 0
for i in range(1, N):
    if i > 1:
        F[i] = min(F[i-1]+abs(H[i] - H[i-1]), F[i-2]+abs(H[i] - H[i-2]))
    else:
        F[i] = F[i-1]+abs(H[i] - H[i-1])
print(F[-1])
