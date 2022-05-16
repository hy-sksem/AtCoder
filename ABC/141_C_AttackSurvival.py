# https://atcoder.jp/contests/abc141/tasks/abc141_c

N, K, Q = map(int, input().split())
point = [K - Q] * N
for i in range(Q):
    a = int(input())
    point[a - 1] += 1

for j in point:
    if j > 0:
        print("Yes")
    else:
        print("No")
