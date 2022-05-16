N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
mod = 10**9 + 7

ans = 1
for i in range(N):
    ans *= A[i][0] + A[i][1] + A[i][2] + A[i][3] + A[i][4] + A[i][5]
    ans %= mod

print(ans)
