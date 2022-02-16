import math

n, r = map(int, input().split())
print(int(math.factorial(n) / (math.factorial(r) * math.factorial(n-r))))
