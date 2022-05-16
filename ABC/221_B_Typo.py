S = input()
T = input()

dif_i = []
dif_l = [[], []]
for i, (s, t) in enumerate(zip(S, T)):
    if s == t:
        continue
    else:
        dif_i.append(i)
        dif_l[0].append(s)
        dif_l[1].append(t)
        if len(dif_i) > 2:
            print("No")
            exit()
if set(dif_l[0]) == set(dif_l[1]):
    if dif_i and dif_i[1] - dif_i[0] != 1:
        print("No")
        exit()
    print("Yes")
else:
    print("No")
