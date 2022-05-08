import bisect

N, Q = map(int, input().split())
A = sorted(list(map(int, input().split())))
for i in range(Q):
    x = int(input())
    print(N - bisect.bisect_left(A, x))
