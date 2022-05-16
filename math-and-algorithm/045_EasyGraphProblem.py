N, M = map(int, input().split())
G = [list() for i in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

ans = 0
for i in range(1, N + 1):
    cnt = 0
    for j in G[i]:
        if j < i:
            cnt += 1
    if cnt == 1:
        ans += 1
print(ans)
