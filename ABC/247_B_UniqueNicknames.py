N = int(input())
s = [None] * N
t = [None] * N
for i in range(N):
    s[i], t[i] = input().split()

for i in range(N):
    flag_s = False
    flag_t = False
    for j in range(N):
        if j == i:
            continue
        if s[i] == s[j] or s[i] == t[j]:
            flag_s = True
        if t[i] == t[j] or t[i] == s[j]:
            flag_t = True
    if flag_s and flag_t:
        print("No")
        exit()
print("Yes")
