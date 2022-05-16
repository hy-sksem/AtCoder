# https://atcoder.jp/contests/abc152/tasks/abc152_c

N = int(input())
P = list(map(int, input().split()))

low = 200001
cnt = 0
for p in P:
    if p <= low:
        cnt += 1
        low = p
    else:
        continue
print(cnt)
