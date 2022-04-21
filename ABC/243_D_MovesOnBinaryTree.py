N, X = map(int, input().split())
S = input()

short_s = []
for s in S:
    if s == "U" and len(short_s) > 0 and (short_s[-1] != "U"):
        short_s.pop()
    else:
        short_s.append(s)

for s in short_s:
    if s == "U":
        X //= 2
    if s == "L":
        X *= 2
    if s == "R":
        X = X * 2 + 1
print(X)
