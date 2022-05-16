# https://atcoder.jp/contests/abc140/tasks/abc140_b

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

forward = 0
ans = 0
for a in A:
    ans += B[a - 1]
    if a - 1 == forward and forward != 0:

        ans += C[forward - 1]
    forward = a
print(ans)
