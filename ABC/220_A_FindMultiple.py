a, b, c = map(int, input().split())

for i in range(1, 1000):
    n = c * i
    if a <= n and n <= b:
        print(n)
        exit()
    else:
        continue
print(-1)
