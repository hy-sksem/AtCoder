# https://atcoder.jp/contests/abc186/tasks/abc186_b

h, w = map(int, input().split())
a = [list(map(int, input().split())) for i in range(h)]

min_a = 100
ans = 0
for i in a:
    if min(i) < min_a:
        min_a = min(i)
for j in a:
    for k in j:
        if k > min_a:
            ans += k - min_a
print(ans)