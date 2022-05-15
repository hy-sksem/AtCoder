from itertools import combinations

N, W = map(int, input().split())
A = list(map(int, input().split()))

ans = set()
for i in combinations(A, 3):
    if sum(i) <= W:
        ans.add(sum(i))
for i in combinations(A, 2):
    if sum(i) <= W:
        ans.add(sum(i))
for i in combinations(A, 1):
    if sum(i) <= W:
        ans.add(sum(i))
print(len(ans))
