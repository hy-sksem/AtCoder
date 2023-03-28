from math import gcd

N, A, B = map(int, input().split())
q = N // A
sum_a = (A + A * q) * q // 2
q = N // B
sum_b = (B + B * q) * q // 2
q = N // ((A * B) // gcd(A, B))
sum_ab = (((A * B) // gcd(A, B)) + ((A * B) // gcd(A, B)) * q) * q // 2

if A != B and max(A, B) % min(A, B) != 0:
    print(sum(range(N + 1)) - sum_a - sum_b + sum_ab)
else:
    print(sum(range(N + 1)) - max(sum_a, sum_b))
