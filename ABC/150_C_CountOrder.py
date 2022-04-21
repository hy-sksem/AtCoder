# https://atcoder.jp/contests/abc150/tasks/abc150_c

import itertools
N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
P_s = sorted(P)
l = list(itertools.permutations(P_s))
print(abs(l.index(tuple(P)) - l.index(tuple(Q))))
