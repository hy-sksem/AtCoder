# https://atcoder.jp/contests/abc185/tasks/abc185_b

n, m, t = map(int, input().split())
charge = [list(map(int, input().split())) for i in range(m)]

max = n
l = 0
for i, c in enumerate(charge):
    n -= c[0] - charge[i - 1][1] if i > 0 else c[0]
    if n <= 0:
        print("No")
        exit()
    n += c[1] - c[0]
    if n > max:
        n = max
    l = c[1]

print("Yes") if n - (t - l) > 0 else print("No")
