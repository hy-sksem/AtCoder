S = list(input())

min_s = "".join(S)
max_s = "".join(S)
for i in range(len(S) - 1):
    S.append(S[0])
    S.pop(0)
    min_s = min(min_s, "".join(S))
    max_s = max(max_s, "".join(S))
print(min_s)
print(max_s)
