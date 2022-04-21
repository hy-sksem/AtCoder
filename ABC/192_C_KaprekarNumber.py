# https://atcoder.jp/contests/abc192/tasks/abc192_c

def func(x):
    g1 = int(''.join(sorted(str(x), reverse = True)))
    g2 = int(''.join(sorted(str(x))))
    return g1-g2

N, K = map(int, input().split())
a = func(N)
for j in range(K-1):
    a = func(a)
print(a if K != 0 else N)
