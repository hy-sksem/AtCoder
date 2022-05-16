# https://atcoder.jp/contests/abc189/tasks/abc189_b

from decimal import Decimal

N, X = map(int, input().split())
VP = [list(map(int, input().split())) for _ in range(N)]

al = Decimal("0")
i = 0
for v, p in VP:
    i += 1
    al += Decimal(str(v * p / 100))
    if al > X:
        print(i)
        exit()
print(-1)
