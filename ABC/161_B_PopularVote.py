# https://atcoder.jp/contests/abc161/tasks/abc161_b

N, M = map(int, input().split())
A = list(map(int, input().split()))

a = sorted(A, reverse=True)
print("Yes") if a[M - 1] * 4 * M >= sum(A) else print("No")
