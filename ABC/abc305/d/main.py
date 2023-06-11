from bisect import bisect_right

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
lr = [list(map(int, input().split())) for _ in range(Q)]

B = [0] * N

for i in range(1, N):
    if i % 2 == 0:
        B[i] = B[i - 1] + A[i] - A[i - 1]
    else:
        B[i] = B[i - 1]

for l, r in lr:
    ll = bisect_right(A, l) - 1
    rr = bisect_right(A, r) - 1
    ans = B[rr] - B[ll]
    if ll % 2 == 1:
        ans -= l - A[ll]
    if rr % 2 == 1:
        ans += r - A[rr]
    print(ans)
