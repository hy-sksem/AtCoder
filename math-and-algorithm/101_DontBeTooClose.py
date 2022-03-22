def modpow(a, b, m):
    p = a
    ans = 1
    for i in range(30):
        if b & (1 << i) != 0:
            ans = (ans * p) % m
        p = (p * p) % m
    return ans


def division(a, b, m):
    return (a * modpow(b, m - 2, m)) % m


def ncr(n, r):
    global fact, MOD
    return division(fact[n], (fact[r] * fact[n - r]) % MOD, MOD)


MOD = 10**9 + 7
LIMIT = 10**5

fact = [None] * (LIMIT + 1)
fact[0] = 1
for i in range(1, LIMIT + 1):
    fact[i] = fact[i - 1] * i % MOD

N = int(input())
for i in range(1, N + 1):
    ans = 0
    for j in range(1, (N - 1) // i + 2):
        ans += ncr(N - (i - 1) * (j - 1), j)
        ans %= MOD
    print(ans)
