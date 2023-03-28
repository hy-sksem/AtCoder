from collections import deque


def bfs(s):
    q = deque()
    q.append(s)
    visit = [0] * (N + 1)
    visit[s] = 1
    ans = 0
    while q:
        i = q.popleft()
        ans += y[i]
        for j in G[i]:
            if not visit[j]:
                q.append(j)
                visit[j] = 1
    return ans


N = int(input())
G = [[] for _ in range(N + 1)]
y = [0] * N
for i in range(N):
    a = list(map(int, input().split()))
    y[i] = a[0]
    for j in range(2, len(a)):
        G[i].append(a[j] - 1)
ans = bfs(N - 1)
print(ans)
