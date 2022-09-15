ascii_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def LCS(x, y):
    pm = dict((zip(ascii_letters, [0] * 52)))
    for c in pm:
        for i, xc in enumerate(x):
            if c == xc:
                pm[c] |= 1 << i

    V = (1 << len(x)) - 1

    for yc in y:
        V = (V + (V & pm[yc])) | (V & ~pm[yc])

    ans = bin(V)[-len(x) :].count("0")

    return ans


q = int(input())


for i in range(q):
    x = input()
    y = input()
    print(LCS(x, y))
