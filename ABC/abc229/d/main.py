S = input()
K = int(input())
n = len(S)

sum_s = [0] * (n + 1)
for i, s in enumerate(S):
    if s == ".":
        sum_s[i + 1] = sum_s[i] + 1
    else:
        sum_s[i + 1] = sum_s[i]

ans = 0
r = 0
for l in range(n):
    while r <= n - 1 and sum_s[r + 1] - sum_s[l] <= K:
        r = r + 1
    ans = max(ans, r - l)
print(ans)
