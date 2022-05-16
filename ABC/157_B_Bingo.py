# https://atcoder.jp/contests/abc157/tasks/abc157_b

import numpy as np

A = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
b = [int(input()) for _ in range(N)]
cnt = np.zeros((3, 3))
for i in b:
    for j, a in enumerate(A):
        for k, aa in enumerate(a):
            if i == aa:
                cnt[j][k] = 1
            else:
                continue

column_sum = np.sum(cnt, axis=0)
row_sum = np.sum(cnt, axis=1)
if 3 in column_sum or 3 in row_sum:
    print("Yes")
elif (
    cnt[0][0] == cnt[1][1] == cnt[2][2] == 1 or cnt[0][2] == cnt[1][1] == cnt[2][0] == 1
):
    print("Yes")
else:
    print("No")
