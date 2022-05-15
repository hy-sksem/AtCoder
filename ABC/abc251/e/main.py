N = int(input())
A = list(map(int, input().split()))

inf = float("inf")
# 1をあげない場合
dp0 = [[inf] * 2 for _ in range(N)]
dp0[0][0] = 0

for i in range(1, N):
    dp0[i][0] = dp0[i - 1][1]
    dp0[i][1] = min(dp0[i - 1][0], dp0[i - 1][1]) + A[i]

ans = dp0[-1][1]

# 1をあげる場合
dp1 = [[inf] * 2 for _ in range(N)]
dp1[0][1] = A[0]

for i in range(1, N):
    dp1[i][0] = dp1[i - 1][1]
    dp1[i][1] = min(dp1[i - 1][0], dp1[i - 1][1]) + A[i]

ans = min(ans, dp1[-1][0], dp1[-1][1])
print(ans)
