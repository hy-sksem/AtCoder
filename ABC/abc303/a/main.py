N = int(input())
S = input()
T = input()

for s, t in zip(S, T):
    if s == t:
        continue
    elif s == "1" and t == "l" or s == "l" and t == "1":
        continue
    elif s == "0" and t == "o" or s == "o" and t == "0":
        continue
    else:
        exit(print("No"))
print("Yes")
