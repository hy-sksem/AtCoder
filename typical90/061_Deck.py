from collections import deque

dq = deque()
Q = int(input())
for i in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        dq.appendleft(x)
    if t == 2:
        dq.append(x)
    if t == 3:
        print(dq[x - 1])
