from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

d = defaultdict(int)
ans = []
for a in A:
    d[a] += 1
    if d[a] == 2:
        ans.append(a)
print(*ans)
