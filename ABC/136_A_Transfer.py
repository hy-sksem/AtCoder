# https://atcoder.jp/contests/abc136/tasks/abc136_a

A, B, C = map(int, input().split())
print(max(C - (A - B), 0))
