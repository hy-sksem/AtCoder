# https://atcoder.jp/contests/abc179/tasks/abc179_b

n = int(input())
deme = [list(map(int, input().split())) for i in range(n)]
cnt = 0
for d in deme:
    if d[0] == d[1]:
        cnt += 1
        if cnt >= 3:
            print("Yes")
            exit()
    else:
        cnt = 0
print("No")