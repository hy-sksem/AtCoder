from collections import defaultdict

L, N1, N2 = map(int, input().split())
row1 = defaultdict(list)
row2 = defaultdict(list)

idx = 1
for _ in range(N1):
    a, b = map(int, input().split())
    row1[a].append((idx, idx + b - 1))
    idx += b

idx = 1
for _ in range(N2):
    a, b = map(int, input().split())
    row2[a].append((idx, idx + b - 1))
    idx += b


ans = 0
for k, v in row1.items():
    if k in row2:
        i, j = 0, 0
        while i < len(v) and j < len(row2[k]):
            a, b = v[i]
            c, d = row2[k][j]
            if b < c:
                i += 1
            elif d < a:
                j += 1
            else:
                ans += min(b, d) - max(a, c) + 1
                if b < d:
                    i += 1
                else:
                    j += 1

print(ans)
