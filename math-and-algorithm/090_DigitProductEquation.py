def product(m):
    if m == 0:
        return 0
    ans = 1
    while m >= 1:
        ans *= m % 10
        m //= 10
    return ans


def func(digit, m):
    if digit == 11:
        return {product(m)}

    min_value = m % 10
    ret = set()
    for i in range(min_value, 10):
        r = func(digit + 1, m * 10 + i)
        for j in r:
            ret.add(j)
    return ret


N, B = map(int, input().split())
fm_cand = func(0, 0)

ans = 0
for fm in fm_cand:
    m = fm + B
    prod_m = product(m)
    if m - prod_m == B and m <= N:
        ans += 1

print(ans)
