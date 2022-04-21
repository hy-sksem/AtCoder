# https://atcoder.jp/contests/abc175/tasks/abc175_a

s = input()
ans = 0
flag = True
for i in s:
    if i == "R" and flag:
        ans += 1
    elif i == "R":
        ans = 1 if ans == 0 else ans
        flag = True
    else:
        flag = False
print(ans)
