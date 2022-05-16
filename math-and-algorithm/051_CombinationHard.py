def modpow(x, y, m):
    p = x
    ans = 1
    for i in range(30):
        if y & (1 << i):
            ans = (ans * p) % m
        p = (p * p) % m
    return ans


def division(a, b, m):
    return (a * modpow(b, m - 2, m)) % m


MOD = 10**9 + 7

X, Y = map(int, input().split())

bunshi, bunbo = 1, 1
for i in range(1, X + Y + 1):
    bunshi = (bunshi * i) % MOD
for i in range(1, X + 1):
    bunbo = (bunbo * i) % MOD
for i in range(1, Y + 1):
    bunbo = (bunbo * i) % MOD

print(division(bunshi, bunbo, MOD))
