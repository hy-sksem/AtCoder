# https://atcoder.jp/contests/abc196/tasks/abc196_a

a, b = map(int, input().split())
c, d = map(int, input().split())

print(max(max((b-d, b-c)), max((a-d, a-c))))