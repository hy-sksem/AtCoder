# https://atcoder.jp/contests/abc186/tasks/abc186_c

n = int(input())
ans = 0
for i in range(1, n + 1):
    i_s = str(i)
    oct_s = oct(i)
    if "7" in i_s or "7" in oct_s:
        continue
    else:
        ans += 1
print(ans)
