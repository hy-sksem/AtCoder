# https://atcoder.jp/contests/abc174/tasks/abc174_b

n, D = map(int, (input().split()))
xy = [list(map(int, input().split())) for i in range(n)]
xy_d = []
for i in xy:
    d = pow(pow(i[0], 2) + pow(i[1], 2), 0.5)
    if d <= D:
        xy_d.append(d)

print(len(xy_d))
