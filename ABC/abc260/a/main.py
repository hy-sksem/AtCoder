from collections import Counter

S = Counter(list(input()))
for k, v in S.items():
    if v == 1:
        print(k)
        exit()
print(-1)
