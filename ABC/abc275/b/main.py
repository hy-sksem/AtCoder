A, B, C, D, E, F = map(int, input().split())
mod = 998244353


def solve(x, y, z):
    return (x % mod) * (y % mod) * (z % mod)


print((solve(A, B, C) - solve(D, E, F)) % mod)
