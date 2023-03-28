a, b, c = map(int, input().split())
a, b, c = sorted([a, b, c])
if a + b < c:
    print(-1)
else:
    print(c)
