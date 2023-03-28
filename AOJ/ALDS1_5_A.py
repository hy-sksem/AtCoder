N = int(input())
A = list(map(int, input().split()))
Q = int(input())
M = list(map(int, input().split()))

df = [False] * 2001
for i in range(1, 1 << N):
    tmp = 0
    for j in range(N):
        if (i >> j) & 1:
            tmp += A[j]
    df[tmp] = True

for m in M:
    print("yes" if df[m] else "no")
