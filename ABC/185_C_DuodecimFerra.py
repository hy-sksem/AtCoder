# https://atcoder.jp/contests/abc185/tasks/abc185_c

from scipy.special import comb
l = int(input())
c = comb(l-1, 11, exact=True)
print(c)
