# https://atcoder.jp/contests/abc157/tasks/abc157_c

N, M = map(int, input().split())
sc = [list(map(int, input().split())) for _ in range(M)]
ans_l = [False] * N
for s, c in sc:
    if ans_l[s - 1] and ans_l[s - 1] != c:
        print(-1)
        exit()
    elif N > 1 and s == 1 and c == 0:
        print(-1)
        exit()
    else:
        ans_l[s - 1] = c
ans = 0
for j, a in enumerate(ans_l):
    if not a:
        if N > 1 and j == 0:
            ans += 1 * (10 ** (N - 1 - j))
    else:
        ans += a * (10 ** (N - 1 - j))
print(ans)
