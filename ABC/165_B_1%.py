# https://atcoder.jp/contests/abc165/tasks/abc165_b

X = int(input())

D = 100
Y = 0
while D < X:
    Y += 1
    D += D // 100
print(Y)
