# https://atcoder.jp/contests/abc135/tasks/abc135_a

A, B = map(int, input().split())
if (A + B) % 2 == 0:
    print(int((A + B) / 2))
else:
    print("IMPOSSIBLE")
