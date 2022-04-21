# https://atcoder.jp/contests/abc168/tasks/abc168_b

k = int(input())
s = input()
if len(s) <= k:
    print(s)
elif len(s) > k:
    s = s[0:k] + "..."
    print(s)