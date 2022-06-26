import bisect


N = int(input())
S = input()
W = list(map(int, input().split()))

adults = []
children = []
for i in range(N):
    if S[i] == "1":
        adults.append(W[i])
    else:
        children.append(W[i])

adults = sorted(adults)
children = sorted(children)
if not adults or not children:
    print(max(len(adults), len(children)))
    exit()
ans = 0
if len(adults) >= len(children):
    for i in range(len(children) - 1, -1, -1):
        l_index = bisect.bisect_left(adults, children[i] + 1)
        ans = max(ans, i + 1 + len(adults) - l_index)
    if ans < len(adults):
        ans = len(adults)
else:
    for i in range(len(adults)):
        r_index = bisect.bisect_right(children, adults[i] - 1)
        ans = max(ans, len(adults) - i + r_index)
    if ans < len(children):
        ans = len(children)
print(ans)
