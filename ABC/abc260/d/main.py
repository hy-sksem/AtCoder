from bisect import bisect_left
from collections import defaultdict, deque

N, K = map(int, input().split())
P = list(map(int, input().split()))

ans = [-1] * (N + 1)
field_d = defaultdict(list)
field = deque()
for i in range(N):
    # print("P[i]", P[i])

    idx = bisect_left(field, P[i])
    if idx == 0 and len(field) == 0:
        field.appendleft(P[i])
        field_d[P[i]].append(P[i])
    elif idx == len(field):
        field.append(P[i])
        field_d[P[i]].append(P[i])
    else:
        field_d[P[i]] = field_d.pop(field[idx])
        field_d[P[i]].append(P[i])
        field[idx] = P[i]
    if len(field_d[P[i]]) == K:
        for f in field_d[P[i]]:
            ans[f] = i + 1
        field.remove(P[i])
    # print("field_d", field_d)
    # print("field", field)
for a in ans[1:]:
    print(a)
