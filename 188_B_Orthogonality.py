# https://atcoder.jp/contests/abc188/tasks/abc188_b

import numpy as np
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

d = np.dot(A, B)
print("Yes") if d == 0 else print("No")