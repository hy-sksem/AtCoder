D = int(input())
N = int(input())
d = [0] * (D + 2)
for i in range(N):
    l, r = map(int, input().split())
    d[l] += 1
    d[r + 1] -= 1
s = [0] * (D + 1)
for i in range(1, D + 1):
    s[i] = s[i - 1] + d[i]
print(*s[1:], sep="\n")
