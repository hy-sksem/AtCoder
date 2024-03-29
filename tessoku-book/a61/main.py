from collections import defaultdict

N, M = map(int, input().split())
d = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)
for i in range(1, N + 1):
    print(f"{i}: {''.join(sorted(d[i]).__str__()).replace('[', '{').replace(']', '}')}")
