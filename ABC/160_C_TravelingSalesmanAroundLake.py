# https://atcoder.jp/contests/abc160/tasks/abc160_c

import numpy as np

K, N = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
A.append(A[0] + K)
a_diff = np.diff(A)
print(A)
print(a_diff)
print(K - max(a_diff))
