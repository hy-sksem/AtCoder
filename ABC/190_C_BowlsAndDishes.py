# https://atcoder.jp/contests/abc190/tasks/abc190_c

import itertools
N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
K = int(input())
CD = [list(map(int, input().split())) for _ in range(K)]

ans = 0
for ite in itertools.product([0,1], repeat=K):
    dishes = [0]*(N+1)
    for i, j in enumerate(ite):
        dishes[CD[i][j]] = 1
    print(dishes)
    cnt = 0
    for a, b in AB:
        if dishes[a] == 1 and dishes[b] == 1:
            cnt += 1
    ans = max(ans, cnt)
print(ans)