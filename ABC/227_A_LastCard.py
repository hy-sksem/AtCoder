N, K, A = map(int, input().split())

ans = A
for i in range(K-1):
    if ans + 1 > N:
        ans = 0
    ans += 1

print(ans)
