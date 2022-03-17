L, R = map(int, input().split())

prime = [True] * (R - L + 1)
if L == 1:
    prime[0] = False

LIMIT = int(R**0.5)
for i in range(2, LIMIT + 1):
    min_value = ((L + i - 1) // i) * i
    for j in range(min_value, R + 1, i):
        if j == i:
            continue
        prime[j - L] = False

ans = 0
for i in range(R - L + 1):
    if prime[i]:
        ans += 1
print(ans)
