# https://atcoder.jp/contests/abc177/tasks/abc177_b

s = input()
t = input()
ans = 0
for i, j in enumerate(s):
    if i <= len(s) - len(t):
        s2 = s[i : i + len(t)]
        cnt = 0
        for k, l in enumerate(t):
            if l == s2[k]:
                cnt += 1
            ans = cnt if ans < cnt else ans
print(len(t) - ans)
