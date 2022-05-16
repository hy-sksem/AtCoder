def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


from decimal import Decimal

N = int(input())
D = make_divisors(N)
print(D)
cnt = 0
for d in D:
    print("a", d, N)
    print(Decimal(str(((2 * N) / d - (d - 1)))))
    print(Decimal(str(((2 * N) / d))))
    print(Decimal(str((d - 1))))
    print("b")
    x = Decimal(str(((2 * N) / d - (d - 1)) / 2))
    print(float(x))
    if float(x).is_integer():
        cnt += 1
    # if is_int(float(x)):
    #     print("Yes")
    #     cnt += 1
print(cnt)
