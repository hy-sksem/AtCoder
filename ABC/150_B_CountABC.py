# https://atcoder.jp/contests/abc150/tasks/abc150_b

N = int(input())
S = input()
t = "ABC"
a = ""
ans = 0
for s in S:
    a += s
    if len(a) > 3:
        a = a[1:]
    if t == a:
        ans += 1
print(ans)