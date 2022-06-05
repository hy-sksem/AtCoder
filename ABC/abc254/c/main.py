from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))
d = defaultdict(list)

for i, a in enumerate(A):
    d[a].append(i)  # 各数字のindexを格納

srt = sorted(A)
for i, a in enumerate(srt):
    for j in d[a]:
        if j % K == i % K:  # 移動可能
            d[a].pop(d[a].index(j))
            break

for k, v in d.items():
    if v:
        print("No")
        exit()

print("Yes")
