# https://atcoder.jp/contests/abc173/tasks/abc173_c

import itertools
h, w, k = map(int, input().split())
c = [list(input()) for i in range(h)]
ans = 0
for ite in itertools.product([0,1], repeat=h+w):
    cnt = 0
    for i in range(h):
        for j in range(w):
            if ite[i] == 1 or ite[j + h] == 1:
                pass
            else:
                if c[i][j] == "#":
                    cnt += 1
    if cnt == k:
        ans += 1
print(ans)