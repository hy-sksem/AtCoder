S = list(input())
word = "atcoder"

cnt = 0
for i, w in enumerate(word):
    idx = S.index(w)
    for j in range(idx, i, -1):
        S[j], S[j - 1] = S[j - 1], S[j]
    cnt += abs(i - idx)
print(cnt)
