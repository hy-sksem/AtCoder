from collections import defaultdict

N, A, B = map(int, input().split())
d = defaultdict(list)

for i in range(N):
    S = input()
    for j in range(N):
        if S[j] == "o":
            d[i].append(j)
            d[j].append(i)
print("Yes" if B in d[A] else "No")
