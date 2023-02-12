N, M = map(int, input().split())
A = list(map(int, input().split()))

ans = []
tmp = []
for i in range(1, N + 1):
    if i not in A:
        tmp.insert(0, i)
        ans += tmp
        tmp = []
    else:
        tmp.insert(0, i)
print(*ans)
