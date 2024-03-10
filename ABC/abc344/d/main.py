import re

T = input()
N = int(input())
A = [list(input().split()) for _ in range(N)]

dp = [0] * (N + 1)

reT = re.compile(T)
for a in A:
    for t in a[1:]:
        r = re.findall(reT, t)
        if r:
            dp[int(a[0])] += 1
