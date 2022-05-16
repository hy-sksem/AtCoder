# https://atcoder.jp/contests/abc156/tasks/abc156_b

import math

N, K = map(int, input().split())
x = math.log(N, K) if N != 1 else 1
print(math.ceil(x))
