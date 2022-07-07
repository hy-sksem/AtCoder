from math import gcd

L, R = map(int, input().split())

for d in range(R - L, 0, -1):
    for i in range(L, R - d + 1):
        j = i + d
        # print("d:", d, "i:", i, "j:", j)
        if gcd(i, j) == 1:
            print(d)
            exit()
