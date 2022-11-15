T = int(input())
N = int(input())
e = [0] * (T + 2)
for i in range(N):
    l, r = map(int, input().split())
    e[l] += 1
    e[r] -= 1

s = [0] * (T + 1)
for i in range(1, T + 1):
    s[i] = s[i - 1] + e[i - 1]
print(*s[1:], sep="\n")
