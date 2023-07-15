N = int(input())
A = list(map(int, input().split()))

ans = []
tmp = 0
cnt = 0
for a in A:
    cnt += 1
    tmp += a
    if cnt == 7:
        ans.append(tmp)
        cnt = 0
        tmp = 0
if cnt > 0:
    ans.append(tmp)
print(*ans)
