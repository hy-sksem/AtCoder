import math


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


N = int(input())

# A * B + C * D = N の個数を求める
ans = 0
for i in range(1, math.ceil(N // 2) + 1):
    x, y = i, N - i
    ans += len(make_divisors(x)) * len(make_divisors(y))

ans *= 2
if N % 2 == 0:
    ans -= len(make_divisors(N // 2)) ** 2
print(ans)
