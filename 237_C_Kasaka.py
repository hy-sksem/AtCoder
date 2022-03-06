S = input()

x = 0
for i in range(len(S)):
    if S[i] == "a":
        x += 1
    else:
        break

y = 0
for i in range(len(S) - 1, 0, -1):
    if S[i] == "a":
        y += 1
    else:
        break

if x == len(S):
    print("Yes")
    exit()
elif x > y:
    print("No")
    exit()

for i in range(x, len(S) - y - 1):
    if S[i] != S[x + len(S) - y - i - 1]:
        print("No")
        exit()

print("Yes")
