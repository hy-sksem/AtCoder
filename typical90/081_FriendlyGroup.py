N, K = map(int, input().split())

s = [[0] * 5001 for _ in range(5001)]
for i in range(N):
    a, b = map(int, input().split())
    s[a][b] += 1
    if a + K + 1 <= 5000:
        s[a + K + 1][b] -= 1
    if b + K + 1 <= 5000:
        s[a][b + K + 1] -= 1
    if a + K + 1 <= 5000 and b + K + 1 <= 5000:
        s[a + K + 1][b + K + 1] += 1

for i in range(5000):
    for j in range(5000):
        s[i][j + 1] += s[i][j]

for i in range(5000):
    for j in range(5000):
        s[i + 1][j] += s[i][j]
ans = 0
for i in range(5001):
    for j in range(5001):
        ans = max(ans, s[i][j])
print(ans)
