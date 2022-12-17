from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
A = sorted(A)

for _ in range(Q):
    x = int(input())
    print(bisect_left(A, x))
