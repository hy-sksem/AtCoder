n = int(input())
c = list(map(int, input().split()))
c.sort()
ans = 1
for i, j in enumerate(c):
    ans = ans * max(0, j - i) % 1000000007
print(ans)
