S = input()

ans = ""
cnt = 0
for s in S:
    if s == "|":
        cnt += 1
        continue
    if cnt != 1:
        ans += s
print(ans)