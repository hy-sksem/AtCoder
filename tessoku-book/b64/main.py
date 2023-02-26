from heapq import heappush, heappop


N, M = map(int, input().split())
g = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    g[a - 1].append((b - 1, c))
    g[b - 1].append((a - 1, c))

INF = 10**18
cost = [INF] * N
back = [-1] * N
q = []


def push(prev: int, i: int, c: int):
    if cost[i] > c:
        cost[i] = c
        back[i] = prev
        heappush(q, (c, i))


push(-1, N - 1, 0)
while q:
    c, x = heappop(q)
    if cost[x] != c:
        continue
    for y, d in g[x]:
        push(x, y, c + d)

ans = []
x = 0
while x != -1:
    ans.append(x + 1)
    x = back[x]

print(*ans)
