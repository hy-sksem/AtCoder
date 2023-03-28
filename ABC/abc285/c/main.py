S = list(input())

ans = 0
for i in range(len(S) - 1, -1, -1):
    ans += (ord(S[i]) - 64) * 26 ** (len(S) - i - 1)
print(ans)
