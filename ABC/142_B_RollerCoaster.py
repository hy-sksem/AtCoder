# https://atcoder.jp/contests/abc142/tasks/abc142_b

N, K = map(int, input().split())
h = list(map(int, input().split()))

ans = 0
for i in h:
    if i >= K:
        ans += 1
    else:
        continue
print(ans)