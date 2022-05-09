def Eratosthenes(N):
    isprime = [True] * (N + 1)
    isprime[0], isprime[1] = False, False
    primes = []
    for p in range(2, N + 1):
        if not isprime[p]:
            continue
        primes.append(p)

        q = p * 2
        while q <= N:
            isprime[q] = False
            q += p

    return primes


N = int(input())
primes = Eratosthenes(int(N ** (1 / 3)) + 1)
ans = 0
for i in range(len(primes)):
    for j in range(i + 1, len(primes)):
        if primes[i] * primes[j] ** 3 <= N:
            ans += 1
        else:
            break
print(ans)
