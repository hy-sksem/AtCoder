def modpow(a, b, m):
    p = a
    ans = 1
    for i in range(30):
        if b & (1 << i):
            ans = (ans * p) % m
        p = (p * p) % m
    return ans


def division(a, b, m):
    return (a * modpow(b, m - 2, m)) % m


def ncr(n, r):
    global fact, MOD
    return division(fact[n], (fact[r] * fact[n - r]) % MOD, MOD)


MOD = 10**9 + 7
LIMIT = 2 * 10**6

fact = [None] * (LIMIT + 1)
fact[0] = 1
for i in range(1, LIMIT + 1):
    fact[i] = (fact[i - 1] * i) % MOD

N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    ans += A[i] * ncr(N - 1, i)
    ans %= MOD

print(ans)
