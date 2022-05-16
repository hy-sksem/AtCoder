# https://atcoder.jp/contests/abc157/tasks/abc157_a


def RoundUpDivision(a, b):
    if a % b == 0:
        return int(a // b)
    else:
        return int(a // b + 1)


N = int(input())
print(RoundUpDivision(N, 2))
