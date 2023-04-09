N, D = map(int, input().split())
T = list(map(int, input().split()))

ans = -1
for i in range(N - 1):
    x1, x2 = T[i], T[i + 1]
    if x2 - x1 <= D:
        exit(print(x2))

print(ans)
