def modpow(x, y, m):
    p = x
    ans = 1
    for i in range(30):
        if y & (1 << i):
            ans = (ans * p) % m
        p = (p * p) % m
    return ans

MOD = 10**9 + 7

a, b = map(int, input().split())
print(modpow(a, b, MOD))

# a, b = map(int, input().split())
# print(pow(a, b, 1000000007))