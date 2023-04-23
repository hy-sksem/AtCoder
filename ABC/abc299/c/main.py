N = int(input())
S = input()

ans = -1
cnt = 0
flag = False
for s in S:
    if s == "o":
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
        flag = True
if flag:
    ans = max(ans, cnt)
print(ans if ans > 0 else -1)
