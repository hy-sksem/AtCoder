from decimal import Decimal

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

success = []

for i in range(N):
    a, b = AB[i]
    success.append((Decimal(a) / Decimal(a + b), i + 1))

success.sort(reverse=True, key=lambda x: x[0])
ans = []
for _, i in success:
    ans.append(i)
print(*ans)
