# https://atcoder.jp/contests/abc180/tasks/abc180_b
import math
n = int(input())
x = list(map(int, input().split()))
x = sorted(map(abs, x))

m = sum(x)
e = math.sqrt(sum(list(map(lambda x: x * x, x))))
c = max(x)
print(m, e, c, sep="\n")