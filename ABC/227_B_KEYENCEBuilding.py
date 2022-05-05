N = int(input())
S = list(map(int, input().split()))

x = list()

for i in range(1, 200):
    for j in range(1, 200):
        t = 4 * i * j + 3 * i + 3 * j
        if t <= 1000:
            x.append(t)
x = set(x)
ans = 0
for s in S:
    if s in x:
        ans += 1

print(N - ans)
