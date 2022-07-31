mod = 10**9 + 7

N, Q = map(int, input().split())
xyzw = []
for _ in range(Q):
    x, y, z, w = map(int, input().split())
    xyzw.append((1 << x - 1 | 1 << y - 1 | 1 << z - 1, w))


def ok(k, s):
    for bit, w in xyzw:
        if (w >> k & 1) ^ (s & bit != 0):
            return False
    return True


ans = 1
for k in range(60):
    cnt = 0
    for s in range(1 << N):
        cnt += ok(k, s)
    ans = ans * cnt % mod

print(ans)
