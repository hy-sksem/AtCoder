# https://atcoder.jp/contests/abc163/tasks

N, M  = map(int, input().split())
A = list(map(int, input().split()))
ans = N - sum(A)
print(ans) if ans >= 0 else print(-1)
