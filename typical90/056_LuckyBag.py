N, S = map(int, input().split())
A, B = [0] * N, [0] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())

dp = [[False] * (S + 1) for _ in range(N + 1)]
dp[0][0] = True
for i in range(N):
    for j in range(S - 1):
        if dp[i][j]:
            if j + A[i] <= S:
                dp[i + 1][j + A[i]] = True
            if j + B[i] <= S:
                dp[i + 1][j + B[i]] = True

if not dp[N][S]:
    print("Impossible")
    exit()

now = S
ans = ""
for i in range(N, 0, -1):
    if now >= A[i - 1] and dp[i - 1][now - A[i - 1]]:
        ans = "A" + ans
        now -= A[i - 1]
    elif now >= B[i - 1] and dp[i - 1][now - B[i - 1]]:
        ans = "B" + ans
        now -= B[i - 1]
print(ans)
