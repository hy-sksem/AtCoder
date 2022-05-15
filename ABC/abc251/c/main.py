N = int(input())

submitted = set()
ans = [0, 0]
for i in range(1, N + 1):
    s, t = map(str, input().split())
    t = int(t)
    if s in submitted:
        continue
    submitted.add(s)
    if t > ans[1]:
        ans = [i, t]
print(ans[0])
