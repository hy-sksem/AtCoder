N = int(input())
S = input()
ans = 0

for i in range(10):
    s0 = S.find(str(i))
    if s0 == -1:
        continue
    for j in range(10):
        s1 = S[s0 + 1 :].find(str(j))
        if s1 == -1:
            continue
        for k in range(10):
            s2 = S[s0 + 1 + s1 + 1 :].find(str(k))
            if s2 == -1:
                continue
            ans += 1
print(ans)
