S = input()
ans = -1
for i, s in enumerate(S, start=1):
    if s == "a":
        ans = i
print(ans)
