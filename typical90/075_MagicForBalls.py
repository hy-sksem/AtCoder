from typing import List


def prime_factorization(N) -> List[int]:
    res = []
    while N % 2 == 0:
        res.append(2)
        N //= 2

    for i in range(3, int(N**0.5) + 1, 2):
        while N % i == 0:
            res.append(i)
            N //= i

    if N > 2:
        res.append(N)

    return res


N = int(input())
f = prime_factorization(N)
n = len(f)
ans = 0
if n == 1:
    print(ans)
else:
    while n != 1:
        n = -(-n // 2)
        ans += 1
    print(ans)
