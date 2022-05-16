# https://atcoder.jp/contests/abc142/tasks/abc142_c

N = int(input())
A = list(map(int, input().split()))
ans = [0] * N
for i, a in enumerate(A):
    ans[a - 1] = str(i + 1)

print(" ".join(ans))
