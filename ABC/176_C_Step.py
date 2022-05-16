# https://atcoder.jp/contests/abc176/tasks/abc176_c

n = int(input())
a = list(map(int, input().split()))

ans = 0
for i, j in enumerate(a):
    if j < a[i - 1] and i != 0:
        ans += a[i - 1] - a[i]
        a[i] = a[i - 1]
print(ans)
