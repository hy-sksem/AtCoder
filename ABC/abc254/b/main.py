def solve(x, y, lst):
    if y == 0 or x == y:
        return 1
    return lst[y - 1] + lst[y]


N = int(input())
df = [[] for _ in range(N)]

for i in range(N):
    for j in range(i + 1):
        df[i].append(solve(i, j, df[i - 1]))

for i in range(N):
    print(*df[i])
