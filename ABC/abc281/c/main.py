N = int(input())
S = list(input())

flag = True
for i in range(N):
    if S[i] == '"':
        flag = not (flag)
    if flag and S[i] == ",":
        S[i] = "."
print("".join(S))
