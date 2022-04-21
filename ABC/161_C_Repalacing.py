# https://atcoder.jp/contests/abc161/tasks/abc161_c

N, K = map(int, input().split())
print(min(n%k,(-n)%k))