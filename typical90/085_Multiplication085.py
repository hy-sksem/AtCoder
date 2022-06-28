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


K = int(input())
div = calc_divisors(K)

ans = 0
for i in range(len(div)):
    for j in range(i, len(div)):
        a = div[i]
        b = div[j]
        c = K / (a * b)
        if c < b:
            continue
        if c == int(c):
            ans += 1
print(ans)
