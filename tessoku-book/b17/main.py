N = int(input())
H = [0] + list(map(int, input().split()))

dp = [10**18] * (N + 1)
dp[1] = 0
dp[2] = abs(H[2] - H[1])

for i in range(3, N + 1):
    dp[i] = min(dp[i - 1] + abs(H[i] - H[i - 1]), dp[i - 2] + abs(H[i] - H[i - 2]))

route = [N]
idx = N
while idx > 1:
    if dp[idx - 1] + abs(H[idx] - H[idx - 1]) == dp[idx]:
        route.append(idx - 1)
        idx -= 1
    else:
        route.append(idx - 2)
        idx -= 2

print(len(route))
print(*route[::-1])
