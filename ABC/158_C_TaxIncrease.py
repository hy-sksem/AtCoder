# https://atcoder.jp/contests/abc158/tasks/abc158_c

# 割り切ることができれば-1 余りがある場合は切り捨て
def RoundDownDivision(a, b):
    if a % b == 0:
        return int(a // b - 1)
    else:
        return int(a // b)


def RoundUpDivision(a, b):
    if a % b == 0:
        return int(a // b)
    else:
        return int(a // b + 1)


A, B = map(int, input().split())
min_A, min_B = RoundUpDivision(A, 0.08), RoundUpDivision(B, 0.1)
max_A, max_B = RoundDownDivision(A + 1, 0.08), RoundDownDivision(B + 1, 0.1)
if min_B <= min_A <= max_B:
    print(min_A)
elif min_A <= min_B <= max_A:
    print(min_B)
else:
    print(-1)
