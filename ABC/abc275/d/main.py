from collections import defaultdict, deque

N = int(input())
deq = deque([N])
d = defaultdict(int)
d[0] = 1
ans = 0
while len(deq) > 0:
    n = deq.pop()
    if d[n] > 0:
        ans += d[n]
    else:
        if d[n // 3] > 0 and d[n // 2] > 0:
            d[n] = d[n // 3] + d[n // 2]
            ans += d[n]
        else:
            deq.append(n // 3)
            deq.append(n // 2)
print(ans)
