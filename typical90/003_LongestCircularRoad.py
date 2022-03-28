from collections import deque

N = int(input())
G = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

queue = deque()
queue.append((0, -1))
while queue:
    pos, bpos = queue.popleft()
    for npos in G[pos]:
        if npos == bpos:
            continue
        queue.append((npos, pos))

queue = deque()
queue.append((pos, -1, 0))
while queue:
    pos, bpos, d = queue.popleft()
    d += 1
    for npos in G[pos]:
        if npos == bpos:
            continue
        queue.append((npos, pos, d))

print(d)
