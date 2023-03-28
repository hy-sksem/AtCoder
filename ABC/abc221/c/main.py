N = sorted(input(), reverse=True)
ans = 0
for i in range(1 << len(N)):
    l = 0
    r = 0
    for j in range(len(N)):
        if i & (1 << j):
            l = l * 10 + ord(N[j]) - ord("0")
        else:
            r = r * 10 + ord(N[j]) - ord("0")
    ans = max(ans, l * r)
print(ans)
