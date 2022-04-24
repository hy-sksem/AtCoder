S = input()

l = list()
s = list()
for i in S:
    if i.islower():
        if i in s:
            print("No")
            exit()
        else:
            s.append(i)
    else:
        if i in l:
            print("No")
            exit()
        else:
            l.append(i)
if len(l) > 0 and len(s) > 0:
    print("Yes")
else:
    print("No")
