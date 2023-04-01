N = int(input())
S = input()

flag = S[0]
for s in S[1:]:
    if s != flag:
        flag = s
        continue
    else:
        exit(print("No"))
print("Yes")
