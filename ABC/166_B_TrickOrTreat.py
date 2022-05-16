# https://atcoder.jp/contests/abc166/tasks/abc166_b

N, K = map(int, input().split())
da = [list(map(int, input().split())) for _ in range(K * 2)]
t = set()
for i, j in enumerate(da):
    if i % 2 == 0:
        continue
    else:
        t |= set(j)
print(N - len(t))
