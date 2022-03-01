import queue

H, W = map(int, input().split())
sx, sy = map(int, input().split())
gx, gy = map(int, input().split())
c = [input() for _ in range(H)]
start = (sx-1)*W + sy-1
goal = (gx-1)*W + gy-1

G = [list() for _ in range(H*W)]

for i in range(H):
    for j in range(W-1):
        if c[i][j] == '.' and c[i][j+1] == '.':
            G[i*W+j].append(i*W+j+1)
            G[i*W+j+1].append(i*W+j)

for i in range(H-1):
    for j in range(W):
        if c[i][j] == '.' and c[i+1][j] == '.':
            G[i*W+j].append(i*W+j+W)
            G[i*W+j+W].append(i*W+j)

dist = [-1] * (H*W)
Q = queue.Queue()
dist[start] = 0
Q.put(start)

while not Q.empty():
    u = Q.get()
    for v in G[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            Q.put(v)
print(dist[goal])