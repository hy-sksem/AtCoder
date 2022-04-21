# https://atcoder.jp/contests/abc155/tasks/abc155_c

N = int(input())
S = [input() for _ in range(N)]
S.sort()

max = 0
cnt = 0
f = ""
ans_l = []
for i, s in enumerate(S):
    if s == f:
        cnt += 1
        if cnt == max:
            ans_l.append(s)
        elif cnt > max:
            max = cnt
            ans_l = [s]
    else:
        f = s
        cnt = 1
        if cnt >= max:
            max = cnt
            ans_l.append(s)
for a in ans_l:
    print(a)
