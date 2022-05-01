from itertools import permutations

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
XY = [[True] * N for _ in range(N)]
M = int(input())
for i in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    XY[x][y] = False
    XY[y][x] = False

ans = float("inf")
for i in permutations(range(N)):
    cost = 0
    flag = True
    for j in range(N):
        if (j < N - 1) and (not XY[i[j]][i[j + 1]]):
            flag = False
        cost += A[i[j]][j]
    ans = min(ans, cost) if flag else ans
print(ans if ans != float("inf") else -1)
