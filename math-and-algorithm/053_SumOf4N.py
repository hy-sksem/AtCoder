def modpow(x, y, m):
    p = x
    ans = 1
    for i in range(60):
        if y & (1 << i):
            ans = (ans * p) % m
        p = (p * p) % m
    return ans

def division(a, b, m):
    return (a * modpow(b, m-2, m)) % m

MOD = 10**9 + 7

N = int(input())

V = modpow(4, N+1, MOD) - 1
ans = division(V, 3, MOD)

print(ans)
