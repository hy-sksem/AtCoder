# https://atcoder.jp/contests/abc168/tasks/abc168_c

import math
A, B, H, M = map(int, input().split())
ang = abs((30 * H + 0.5 * M) - 6 * M)
print((A**2 + B**2 - 2*A*B * math.cos(math.radians(ang)))**0.5)