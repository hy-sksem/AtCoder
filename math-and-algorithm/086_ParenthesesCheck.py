N = int(input())
S = input()

depth = 0
flag = True
for s in S:
    if s == "(":
        depth += 1
    else:
        depth -= 1
    if depth < 0:
        flag = False
print("Yes" if flag and depth == 0 else "No")
