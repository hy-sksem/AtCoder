# https://atcoder.jp/contests/abc156/tasks/abc156_c

from decimal import Decimal, ROUND_HALF_UP

N = int(input())
X = list(map(int, input().split()))
X_a = Decimal(sum(X) / N).quantize(Decimal("0"), rounding=ROUND_HALF_UP)
ans = 0
for x in X:
    ans += (x - X_a) ** 2
print(ans)
