# https://atcoder.jp/contests/abc153/tasks/abc153_c

N, K = map(int, input().split())
H = list(map(int, input().split()))
H.sort(reverse=True)
print((sum(H)-sum(H[0:K])))