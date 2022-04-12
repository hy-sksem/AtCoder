from collections import deque

N, Q = map(int, input().split())
A = deque(map(int, input().split()))

for i in range(Q):
    t, x, y = map(int, input().split())
    x -= 1
    y -= 1
    if t == 1:
        A[x], A[y] = A[y], A[x]
    elif t == 2:
        n = A.pop()
        A.appendleft(n)
    else:
        print(A[x])
