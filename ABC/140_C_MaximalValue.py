# https://atcoder.jp/contests/abc140/tasks/abc140_c

N = int(input())
B = list(map(int, input().split()))

A = [0] * N
for i in range(N - 1):
    if i == 0:
        A[i] = B[i]
        A[i + 1] = B[i]
    else:
        if B[i - 1] <= B[i]:
            A[i + 1] = B[i]
        else:
            A[i] = B[i]
            A[i + 1] = B[i]
print(sum(A))
