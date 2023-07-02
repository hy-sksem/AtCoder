N, M = map(int, input().split())
C = list(input().split())
D = list(input().split())
P = list(map(int, input().split()))

ans = 0
for c in C:
    if c in D:
        ans += P[D.index(c) + 1]
    else:
        ans += P[0]
print(ans)
