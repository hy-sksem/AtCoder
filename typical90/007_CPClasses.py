import bisect

N = int(input())
A = sorted(list(map(int, input().split())))
Q = int(input())
B = [int(input()) for _ in range(Q)]
for i in range(Q):
    index = bisect.bisect_left(A, B[i])
    if index >= N:
        print(abs(A[-1] - B[i]))
    elif index == 0:
        print(abs(A[0] - B[i]))
    else:
        print(min(abs(A[index] - B[i]), abs(A[index - 1] - B[i])))
