# https://atcoder.jp/contests/abc149/tasks/abc149_b

A, B, K = map(int, input().split())
if A >= K:
    print(A-K, B)
    exit()
elif B >= K-A:
    print(0, B-(K-A))
else:
    print(0, 0)