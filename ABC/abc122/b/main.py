S = input()
ACGT = ("A", "C", "G", "T")
cnt = 0
ans = 0
for i in range(len(S)):
    if S[i] in ACGT:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
print(max(ans, cnt))
