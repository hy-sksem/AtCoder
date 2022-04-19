N, K = map(int, input().split())
S = input()
c = [dict() for _ in range(N)]
d = dict()

for i in range(N - 1, -1, -1):
    d[S[i]] = i
    for j in range(97, 123):
        j = chr(j)
        if j in d:
            c[i][j] = d[j]
        else:
            c[i][j] = N


ans = []
i = 0
while True:
    for j in range(97, 123):
        j = chr(j)
        if len(ans) + N - c[i][j] >= K:
            ans.append(j)
            i = c[i][j] + 1
            break
    if len(ans) == K:
        break
print("".join(ans))
