from collections import defaultdict

N, M = map(int, input().split())
d = defaultdict(list)
for i in range(M):
    u, v = map(int, input().split())
    d[u].append(v)
    d[v].append(u)
# print(d)
ans = 0
for i in range(N):
    for j in d[i]:
        for k in d[j]:
            if i < j < k and i in d[k]:
                ans += 1
print(ans)
