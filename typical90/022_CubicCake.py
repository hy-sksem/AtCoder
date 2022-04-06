import math

A, B, C = map(int, input().split())
gcd = math.gcd(A, math.gcd(B, C))
print((A // gcd - 1) + (B // gcd - 1) + (C // gcd - 1))
