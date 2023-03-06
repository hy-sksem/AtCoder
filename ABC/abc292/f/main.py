from collections import defaultdict

N, M = map(int, input().split())

indegree = defaultdict(list)
outdegree = defaultdict(list)
add_edge = set()
for _ in range(M):
    u, v = map(int, input().split())
    indegree[v].append(u)
    outdegree[u].append(v)
    for i in indegree[u]:
        if i == v:
            continue
        add_edge.add((i, v))
    for o in outdegree[v]:
        if o == u:
            continue
        add_edge.add((u, o))

ans = 0
while add_edge:
    i, j = add_edge.pop()
    if i in indegree[j]:
        continue
    indegree[j].append(i)
    outdegree[i].append(j)
    for k in indegree[i]:
        if k == j:
            continue
        add_edge.add((k, j))
    ans += 1
print(ans)
