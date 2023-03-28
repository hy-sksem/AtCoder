N = input()[::-1]

ans = 0
for i, n in enumerate(N):
    ans += 2 ** i if int(n) else 0
print(ans)
