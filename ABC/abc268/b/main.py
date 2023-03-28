S = input()
T = input()

if len(S) > len(T):
    print("No")
    exit()

for s, t in zip(S, T):
    if s != t:
        print("No")
        exit()
print("Yes")
