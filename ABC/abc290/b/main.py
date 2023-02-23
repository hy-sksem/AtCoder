N, K = map(int, input().split())
S = input()

ans = ""
cnt = 0
for s in S:
    if cnt >= K:
        ans += "x"
    else:
        if s == "x":
            ans += "x"
        else:
            ans += "o"
            cnt += 1
print(ans)
