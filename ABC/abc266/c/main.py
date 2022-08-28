import numpy as np


def vec(i, j, k):
    i, j, k = np.array(i), np.array(j), np.array(k)
    vec1 = i - j
    vec2 = k - j
    absvec1 = np.linalg.norm(vec1)
    absvec2 = np.linalg.norm(vec2)
    inner = np.inner(vec1, vec2)
    cos = inner / (absvec1 * absvec2)
    rad = np.arccos(cos)
    degree = np.rad2deg(rad)
    return degree


p = [list(map(int, input().split())) for _ in range(4)]
c = [(0, 1, 2), (1, 2, 3), (2, 3, 0), (3, 0, 1)]
cnt = 0
for i, j, k in c:
    degree = vec(p[i], p[j], p[k])
    cnt += degree

print("Yes" if int(cnt) == 360 or int(cnt) == 359 else "No")
