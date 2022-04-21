def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


N = int(input())
X = [None] * N
Y = [None] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())

longest = 0
for i in range(N):
    for j in range(i + 1, N):
        longest = max(longest, distance(X[i], Y[i], X[j], Y[j]))

print(longest)
