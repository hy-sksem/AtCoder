# https://atcoder.jp/contests/abc191/tasks/abc191_d

from math import ceil, floor, sqrt
from decimal import Decimal
def cf(a, b):
    return (ceil(a-b), floor(a+b))

x, y, r = map(Decimal, input().split())
start, end = cf(x, r)
ans = 0
for i in range(start, end+1):
    p = ((r**2)-((x-i)**2)).sqrt()
    bottom, top = cf(y, p)
    ans += (top - bottom) + 1
print(ans)