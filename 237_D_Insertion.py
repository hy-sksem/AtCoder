N = int(input())
S = input()

L = list()
R = list()
for i, s in enumerate(S):
    if s == "L":
        R.append(i)
    else:
        L.append(i)
print(*(L + [N] + R[::-1]))
