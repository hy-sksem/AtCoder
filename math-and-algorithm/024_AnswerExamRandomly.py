N = int(input())

ans = 0
for i in range(N):
    P, Q = map(int, input().split())
    ans += Q/P

print(ans)
