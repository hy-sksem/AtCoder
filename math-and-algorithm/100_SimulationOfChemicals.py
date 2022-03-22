import numpy as np

Q = int(input())
ans = []
for i in range(Q):
    S = input().split()
    X, Y, Z, T = float(S[0]), float(S[1]), float(S[2]), int(S[3])
    A = np.array([[1 - X, Y, 0], [0, 1 - Y, Z], [X, 0, 1 - Z]])
    ans.append(np.linalg.matrix_power(A, T))

for a in ans:
    print("%.15f %.15f %.15f" % (sum(a[0]), sum(a[1]), sum(a[2])))
