# https://atcoder.jp/contests/abc159/tasks/abc159_a

from scipy.special import comb
N, M = map(int, input().split())
c = comb(N+M, 2, exact=True) - ((comb(M, 1, exact=True))*(comb(N, 1, exact=True)))
print(c)