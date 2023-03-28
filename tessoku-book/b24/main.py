from bisect import bisect_left


def LIS(a):
    dp = [a[0]]
    for i in range(1, len(a)):
        if a[i] > dp[-1]:
            dp.append(a[i])
        else:
            dp[bisect_left(dp, a[i])] = a[i]
    return len(dp)


N = int(input())
XY = [None] * N

for i in range(N):
    XY[i] = tuple(map(int, input().split()))

XY.sort(key=lambda x: (x[0], -x[1]))

print(LIS([y for x, y in XY]))
