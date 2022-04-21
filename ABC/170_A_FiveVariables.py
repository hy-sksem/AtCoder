# https://atcoder.jp/contests/abc170/tasks/abc170_a

x = list(map(int, input().split()))
for i, j in enumerate(x):
    if j == 0:
        print(i + 1)
        exit()