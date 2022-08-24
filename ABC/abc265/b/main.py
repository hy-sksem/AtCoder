N, M, T = map(int, input().split())
A = [0] + list(map(int, input().split()))
b = [0] * (N + 1)
for i in range(M):
    x, y = map(int, input().split())
    b[x] = y


for i in range(1, N):
    if T - A[i] <= 0:
        print("No")
        exit()
    T -= A[i]
    T += b[i + 1]

print("Yes")
