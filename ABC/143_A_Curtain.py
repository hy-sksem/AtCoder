# https://atcoder.jp/contests/abc143/tasks/abc143_a

A, B = map(int, input().split())
print(A-2*B if A-2*B>=0 else 0)