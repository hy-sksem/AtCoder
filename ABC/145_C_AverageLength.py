# https://atcoder.jp/contests/abc145/tasks/abc145_c

import math
import itertools


def distance(X, Y):
    return math.sqrt((X[0] - Y[0]) ** 2 + (X[1] - Y[1]) ** 2)


N = int(input())
k = [i for i in range(N)]
xy = [tuple(map(int, input().split())) for _ in range(N)]
l = list(itertools.permutations(k))

ans = 0
for j in range(len(l)):
    cnt = 0
    for k in range(N - 1):
        cnt += distance(xy[l[j][k]], xy[l[j][k + 1]])
    ans += cnt
print(ans / len(l))
