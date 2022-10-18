N, X = map(int, input().split())
A = list(map(int, input().split()))
ans = "No"
for a in A:
    if X == a:
        ans = "Yes"
print(ans)
