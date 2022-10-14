from collections import defaultdict

N, M = map(int, input().split())

d = defaultdict(set)
for i in range(M):
    k, *x = map(int, input().split())
    for j in range(k):
        for l in range(k):
            d[x[j]].add(x[l])

for i in range(1, N + 1):
    if d[i] == set(range(1, N + 1)):
        continue
    else:
        print("No")
        exit()
print("Yes")
