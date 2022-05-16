# https://atcoder.jp/contests/abc144/tasks/abc144_c

import math

N = int(input())
n_r = math.floor(math.sqrt(N))
while True:
    if N % n_r == 0:
        print(int(n_r + (N / n_r) - 2))
        exit()
    else:
        n_r -= 1
