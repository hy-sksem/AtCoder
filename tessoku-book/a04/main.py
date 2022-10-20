N = int(input())
ans = []
for i in range(9, -1, -1):
    w = 2**i
    ans.append(str((N // w) % 2))
print("".join(a for a in ans))
