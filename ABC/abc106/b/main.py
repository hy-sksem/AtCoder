from typing import List


def calc_divisors(N) -> List[int]:
    res = []
    for i in range(1, N + 1):
        if i * i > N:
            break
        if N % i != 0:
            continue
        res.append(i)
        if N // i != i:
            res.append(N // i)
    res.sort()
    return res


N = int(input())
ans = 0
for i in range(1, N + 1, 2):
    if len(calc_divisors(i)) == 8:
        ans += 1
print(ans)
