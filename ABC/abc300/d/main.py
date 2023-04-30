from typing import List


def Eratosthenes(N: int) -> List[int]:
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

    return isprime, primes


def count_numbers(N):
    # 素数のリストを作成する
    isprime, primes = Eratosthenes(int(N**0.5) // 2 + 1)

    c_primes = [0 for _ in range(int(N**0.5) // 2 + 1)]
    for i in range(int(N**0.5) // 2 + 1):
        if isprime[i]:
            c_primes[i] = 1
        c_primes[i] += c_primes[i - 1]
    # a, cを素数から選び、bを候補から選ぶ
    cnt = 0
    for i in range(len(primes)):
        a = primes[i]
        if a**5 > N:
            break
        for j in range(i + 1, len(primes)):
            c = primes[j]
            if a**3 * c**2 > N:
                break
            max_b = int(N / (a**2 * c**2))  # bの最大値を求める
            max_b = min(max_b, c - 1)
            if max_b < a:
                break
            cnt += c_primes[max_b] - c_primes[a]

    return cnt


N = int(input())
print(count_numbers(N))
