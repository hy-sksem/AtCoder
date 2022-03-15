N = int(input())

ans = 10**19
for i in range(1, int(N**0.5) + 1):
    if N % i == 0:
        ans = min(ans, 2 * i + 2 * (N // i))
print(ans)
