# https://atcoder.jp/contests/tessoku-book/tasks/abc007_3
def int1(x: int) -> int:
    return int(x) - 1


def push(x: int, y: int, c: int):
    if G[x][y] == "#":
        return
    if cost[x][y] <= c:
        return
    cost[x][y] = c
    q.append((x, y))


R, C = map(int, input().split())
start = tuple(map(int1, input().split()))
goal = tuple(map(int1, input().split()))
G = [input() for _ in range(R)]

cost = [[10**18] * C for _ in range(R)]

q = []
push(start[0], start[1], 0)
for x, y in q:
    c2 = cost[x][y] + 1
    push(x + 1, y, c2)
    push(x - 1, y, c2)
    push(x, y + 1, c2)
    push(x, y - 1, c2)
print(cost[goal[0]][goal[1]])
