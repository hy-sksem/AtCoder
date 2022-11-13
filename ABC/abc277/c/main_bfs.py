from collections import defaultdict, deque

n = int(input())
d = defaultdict(list)
for _ in range(n):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)

q = deque()
q.append(1)
S = {1}
while q:
    v = q.popleft()
    for i in d[v]:
        if i not in S:
            q.append(i)
            S.add(i)
print(max(S))
