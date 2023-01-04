N, S = map(int, input().split())
A = [0] + list(map(int, input().split()))

dp = [[False] * (S + 1) for _ in range(N + 1)]
dp[0][0] = True

for i in range(1, N + 1):
    for j in range(S + 1):
        if dp[i - 1][j]:
            dp[i][j] = True
            if j + A[i] <= S:
                dp[i][j + A[i]] = True

# Sとなる方法が存在しない場合
if not dp[N][S]:
    exit(print(-1))

choice = []
idx = S
for i in range(N, 0, -1):
    if idx - A[i] >= 0 and dp[i - 1][idx - A[i]]:
        idx -= A[i]
        choice.append(i)
print(len(choice))
print(*choice[::-1])
