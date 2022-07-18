from collections import defaultdict


def ex_red(n):
    cnt = red[n]
    red[n] = 0
    red[n - 1] += cnt
    blue[n] += X * cnt


def ex_blue(n):
    cnt = blue[n]
    blue[n] = 0
    blue[n - 1] += Y * cnt
    red[n - 1] += cnt


N, X, Y = map(int, input().split())
red = defaultdict(int)
blue = defaultdict(int)
red[N] += 1

for i in range(N, 1, -1):
    ex_red(i)
    ex_blue(i)
print(blue[1])
