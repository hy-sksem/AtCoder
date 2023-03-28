N = int(input())
f = 3.5
for _ in range(N - 1):
    tmp = 0
    for i in range(1, 7):
        tmp += max(i, f) / 6
    f = tmp
print(f)
