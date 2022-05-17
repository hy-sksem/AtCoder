N, Q = map(int, input().split())
A = list(map(int, input().split()))

diff = [A[i + 1] - A[i] for i in range(N - 1)]
ans = sum(abs(d) for d in diff)

for i in range(Q):
    l, r, v = map(int, input().split())
    l -= 1
    r -= 1
    if l > 0:
        ans -= abs(diff[l - 1])
        diff[l - 1] += v
        ans += abs(diff[l - 1])
    if r < N - 1:

        ans -= abs(diff[r])
        diff[r] -= v
        ans += abs(diff[r])
    print(ans)
