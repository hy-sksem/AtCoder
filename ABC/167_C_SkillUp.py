# https://atcoder.jp/contests/abc167/tasks/abc167_c

import numpy as np
import itertools
N, M, X = map(int, input().split())
CA = [list(map(int, input().split())) for _ in range(N)]

ans = 10 ** 5 * 12
flag = False
for ite in itertools.product([0,1], repeat=N):
    ca = []
    for i, j in enumerate(ite):
        if j == 1:
            continue
        else:
            ca.append([CA[i]])
    if len(ca) == 0:
        break
    ca_np = np.array(ca)
    s = np.sum(ca, axis=0)
    for k, l in enumerate(s[0]):
        if k == 0:
            continue
        if l < X:
            break
    else:
        flag = True
        ans = s[0][0] if s[0][0] < ans else ans
print(ans) if flag else print(-1)