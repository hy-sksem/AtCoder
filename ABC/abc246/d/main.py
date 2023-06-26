def calc(a, b):
    return a**3 + a**2 * b + a * b**2 + b**3


N = int(input())

ans = 10**18
j = 10**6
for i in range(10**6 + 1):
    while calc(i, j) >= N and j >= 0:
        ans = min(ans, calc(i, j))
        j -= 1
print(ans)
