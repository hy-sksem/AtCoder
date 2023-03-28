import math

A, B = map(int, input().split())
l = 0
r = 10**18
while r - l > 2:
    c1 = (l + l + r) // 3
    c2 = (l + r + r) // 3
    t1 = B * c1 + A / math.sqrt(c1 + 1)
    t2 = B * c2 + A / math.sqrt(c2 + 1)
    # print("lr", l, r)
    # print("c", c1, c2)
    # print("t", t1, t2)
    if t1 > t2:
        l = c1
    else:
        r = c2

ans = 10**18
for i in range(max(0, l - 10000), r + 10000):
    t = B * i + A / math.sqrt(i + 1)
    ans = min(ans, t)
print(f"{ans:.10f}")
