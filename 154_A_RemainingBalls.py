# https://atcoder.jp/contests/abc154/tasks/abc154_a

S, T = map(str, input().split())
A, B = map(int, input().split())
U = input()

if S == U:
    print(A-1, B)
else:
    print(A, B-1)