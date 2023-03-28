N = int(input())
S = input()

pos = set()
X = 0
Y = 0
pos.add((X, Y))
ans = "No"
for s in S:
    if s == "R":
        X += 1
    elif s == "L":
        X -= 1
    elif s == "U":
        Y += 1
    elif s == "D":
        Y -= 1
    if (X, Y) in pos:
        ans = "Yes"
        break
    pos.add((X, Y))
print(ans)
