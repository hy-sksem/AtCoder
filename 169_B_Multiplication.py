# https://atcoder.jp/contests/abc169/tasks/abc169_b

n = int(input())
a = list(map(int, input().split()))

if 0 in a:
    print(0)
    exit()

prod = 1
for i in a:
    prod *= i
    if prod > 10**18:
        print(-1)
        exit()
print(prod)
