# https://atcoder.jp/contests/abc151/tasks/abc151_c

N, M = map(int, input().split())
l = [0] * N
ac_cnt = 0
p_cnt = 0
for i in range(M):
    p, S = map(str, input().split())
    p = int(p)
    if S == "AC" and l[p - 1] >= 0:
        ac_cnt += 1
        p_cnt += l[p - 1]
        l[p - 1] = -1
    elif l[p - 1] < 0:
        continue
    else:
        l[p - 1] += 1
print(ac_cnt, p_cnt)
