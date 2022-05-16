def modpower(x, y, m):
    p = x
    ans = 1
    for i in range(30):
        if y & (1 << i):
            ans = (ans * p) % m
        p = (p * p) % m
    return ans


def division(a, b, m):
    return (a * modpower(b, m - 2, m)) % m


X, Y = map(int, input().split())
MOD = 10**9 + 7

if (2 * Y - X) < 0 or (2 * X - Y) < 0:
    print(0)
elif (2 * Y - X) % 3 != 0 or (2 * X - Y) % 3 != 0:
    print(0)
else:
    bunshi = 1
    bunbo = 1
    a = (2 * Y - X) // 3
    b = (2 * X - Y) // 3
    for i in range(1, a + b + 1):
        bunshi = (bunshi * i) % MOD
    for i in range(1, a + 1):
        bunbo = (bunbo * i) % MOD
    for i in range(1, b + 1):
        bunbo = (bunbo * i) % MOD
    print(division(bunshi, bunbo, MOD))
