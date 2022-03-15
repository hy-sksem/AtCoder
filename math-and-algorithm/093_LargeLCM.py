import math

A, B = map(int, input().split())
L = A * B // math.gcd(A, B)
if L > 10**18:
    print("Large")
else:
    print(L)
