# https://atcoder.jp/contests/abc152/tasks/abc152_b

a, b = map(str, input().split())
l = [a * int(b), b * int(a)]
l.sort()
print(int(l[0]))
