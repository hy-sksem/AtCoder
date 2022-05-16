# https://atcoder.jp/contests/abc136/tasks/abc136_b

N = int(input())

ans = 0
for i in range(1, N + 1):
    s = str(i)
    if len(s) % 2 == 0:
        continue
    else:
        ans += 1
print(ans)
