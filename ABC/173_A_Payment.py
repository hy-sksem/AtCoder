# https://atcoder.jp/contests/abc173/tasks/abc173_a
n = int(input())
i = n % 1000
print(1000 - i) if i != 0 else print(0)
