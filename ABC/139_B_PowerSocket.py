# https://atcoder.jp/contests/abc139/tasks/abc139_b

A, B = map(int, input().split())

cnt = 0
while True:
    print(cnt*(A-1) + 1)
    if cnt*(A-1) + 1 >= B:
        print(cnt)
        exit()
    else:
        cnt += 1
