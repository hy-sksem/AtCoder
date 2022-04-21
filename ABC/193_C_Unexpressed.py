# https://atcoder.jp/contests/abc193/tasks/abc193_c

N = int(input())
sq = int(N ** 0.5)
s = set()
for i in range(2, sq + 1):
    x = i * i
    while x <= N:
        s.add(x)
        x *= i
print(N - len(s))