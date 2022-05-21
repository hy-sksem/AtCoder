N = int(input())
A = list(map(int, input().split()))
size = sum(A)
A += A

now = A[0]
l, r = 0, 0

for l in range(2 * N):
    while now <= size / 10:
        if size / 10 == now:
            print("Yes")
            exit()
        r += 1
        if r > 2 * N - 1:
            print("No")
            exit()
        now += A[r]
    now -= A[l]
print("No")
