from itertools import groupby

N = int(input())
S = input()
gb = groupby(S)
ans = N * (N - 1) // 2
for k, g in gb:
    l = len(list(g))
    ans -= l * (l - 1) // 2
print(ans)
