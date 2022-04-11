from collections import deque

Q = int(input())
d = deque()
for i in range(Q):
    n, *q = input().split()
    if n == "1":
        x, c = q
        x, c = int(x), int(c)
        d.append([c, x])
    elif n == "2":
        c2 = q[0]
        c2 = int(c2)
        flag = True
        ans = 0
        while flag:
            c, x = d.popleft()
            if c == c2:
                ans += c2 * x
                print(ans)
                flag = False
            elif c > c2:
                ans += c2 * x
                print(ans)
                flag = False
                d.appendleft([c - c2, x])
            else:
                ans += c * x
                c2 -= c
