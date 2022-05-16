# https://atcoder.jp/contests/abc188/tasks/abc188_c

N = int(input())
A = list(map(int, input().split()))
half = len(A) / 2
first = A[0 : int(half)]
second = A[int(half) :]
if max(first) > max(second):
    print(A.index(max(second)) + 1)
else:
    print(A.index(max(first)) + 1)
