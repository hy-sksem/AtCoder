# https://atcoder.jp/contests/abc188/tasks/abc188_a

X, Y = map(int, input().split())
print("Yes") if (min(X, Y) + 3) > max(X, Y) else print("No")
