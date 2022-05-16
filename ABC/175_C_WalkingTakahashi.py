# https://atcoder.jp/contests/abc175/tasks/abc175_c

x, k, d = map(int, input().split())
x = abs(x)
if x - k * d == 0:
    print(0)
    exit()
elif x - k * d > 0:
    print(x - k * d)
    exit()
elif x - k * d < 0:
    i = x // d + 1
    if (k - i) % 2 == 0:
        print(abs(x - i * d))
        exit()
    else:
        print(x - (x // d) * d)
