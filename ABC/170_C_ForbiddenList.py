# https://atcoder.jp/contests/abc170/tasks/abc170_c

x, n = map(int, input().split())
if n == 0:
    print(x)
    exit()
p = list(map(int, input().split()))
for i in range(x + 1):
    if not x - i in p:
        print(x - i)
        exit()
    if not x + i in p:
        print(x + i)
        exit()