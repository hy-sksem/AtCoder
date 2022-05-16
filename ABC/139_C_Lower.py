# https://atcoder.jp/contests/abc139/tasks/abc139_c

N = int(input())
H = list(map(int, input().split()))

ans = 0
cnt = 0
forward = 0
for h in H:
    if h <= forward:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
    forward = h
print(max(ans, cnt))
