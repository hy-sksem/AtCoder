# https://atcoder.jp/contests/abc151/tasks/abc151_b

N, K, M = map(int, input().split())
A = list(map(int, input().split()))
if 0 <= M * N - sum(A) <= K:
    print(M * N - sum(A))
elif M * N - sum(A) < 0:
    print(0)
else:
    print(-1)
