N, K = map(int, input().split())
mod = 10**9 + 7
print(K * (K - 1) * pow(K - 2, N - 2, mod) % mod if N > 1 else K)
