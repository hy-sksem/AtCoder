from itertools import groupby

X, Y, Z = map(int, input().split())
S = input()

rle = [[key, len(list(group))] for key, group in groupby(S)]
dp = [[0] * (len(rle) + 1) for _ in range(2)]
dp[1][0] = 10**18
for i in range(len(rle)):
    k, v = rle[i][0], rle[i][1]
    if k == "a":
        dp[0][i + 1] = min(
            # caps off -> caps off
            dp[0][i] + X * v,
            # caps on -> caps off
            dp[1][i] + X * v + Z,
        )
        dp[1][i + 1] = min(
            # caps off -> caps on
            dp[0][i] + Y * v + Z,
            # caps on -> caps on
            dp[1][i] + Y * v,
        )
    elif k == "A":
        dp[0][i + 1] = min(
            # caps off -> caps off
            dp[0][i] + Y * v,
            # caps on -> caps off
            dp[1][i] + Y * v + Z,
        )
        dp[1][i + 1] = min(
            # caps off -> caps on
            dp[0][i] + X * v + Z,
            # caps on -> caps on
            dp[1][i] + X * v,
        )
print(min(dp[0][-1], dp[1][-1]))
