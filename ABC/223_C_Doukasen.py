from decimal import Decimal

n = int(input())
A = []
B = []
t = [0] * n
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    t[i] = Decimal(a) / Decimal(b) + t[i-1]

half = t[-1] / 2
for i, time in enumerate(t):
    if time >= half:
        ans = sum(A[0:i])
        x = half - t[i-1] if i > 0 else half
        ans += x * B[i]
        print(ans)
        exit()
