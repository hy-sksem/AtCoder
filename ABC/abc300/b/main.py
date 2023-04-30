import numpy as np

H, W = map(int, input().split())
A = np.array([list(input()) for _ in range(H)])
B = np.array([list(input()) for _ in range(H)])
for i in range(H):
    for j in range(W):
        if np.array_equal(A, B):
            break
        A = np.roll(A, 1, axis=1)
    if np.array_equal(A, B):
        break
    A = np.roll(A, 1, axis=0)
else:
    exit(print("No"))
print("Yes")
