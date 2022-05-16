# https://atcoder.jp/contests/abc153/tasks/abc153_b

H, N = map(int, input().split())
A = list(map(int, input().split()))

print("Yes") if sum(A) >= H else print("No")
