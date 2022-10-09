N = int(input())
A = list(map(int, input().split()))

if N == 2 and sum(A) % 2 == 1:
    print(-1)
    exit()

A.sort(reverse=True)
f = A[0]
s = A[1]
ans = 0 if (f + s) % 2 == 1 else f + s
for i in range(2, N):
    _f = f + A[i]
    _s = s + A[i]
    if _f % 2 == 0:
        ans = max(ans, _f)
    if _s % 2 == 0:
        ans = max(ans, _s)
print(ans)
