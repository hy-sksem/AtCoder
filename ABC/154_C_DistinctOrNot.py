# https://atcoder.jp/contests/abc154/tasks/abc154_c

N = int(input())
A = list(map(int, input().split()))
A_s = set(A)
print("YES") if len(A) == len(A_s) else print("NO")
