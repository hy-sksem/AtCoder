# https://atcoder.jp/contests/abc143/tasks/abc143_c

N = int(input())
S = input()

f = ""
ans = ""
for i in S:
    if i == f:
        continue
    else:
        ans += i
        f = i
print(len(ans))
