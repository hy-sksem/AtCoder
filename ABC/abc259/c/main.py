S = list(input())
T = list(input())
if len(S) > len(T):
    print("No")
    exit()
collect = []

add_cnt = 0
for i in range(len(T)):
    if i - add_cnt < len(S) and S[i - add_cnt] == T[i]:
        collect.append(T[i])
    elif len(collect) >= 2 and collect[i - 1] == collect[i - 2] == T[i]:
        collect.append(T[i])
        add_cnt += 1
    else:
        print("No")
        exit()
    # print(collect)
if T == collect:
    print("Yes")
else:
    print("No")
