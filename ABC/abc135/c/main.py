# https://atcoder.jp/contests/abc135/tasks/abc135_c

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for i, b in enumerate(B):
    if b <= A[i]:
        ans += b
    elif b <= A[i] + A[i + 1]:
        ans += b
        A[i + 1] -= b - A[i]
    else:
        ans += A[i] + A[i + 1]
        A[i + 1] = 0
print(ans)
