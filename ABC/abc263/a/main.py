from collections import defaultdict

card = list(map(int, input().split()))
d = defaultdict(int)
ans = "Yes"
for c in card:
    d[c] += 1
    if len(d) > 2:
        ans = "No"
        break
    if d[c] > 3:
        ans = "No"
        break
print(ans)
