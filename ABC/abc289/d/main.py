N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
X = int(input())
trap = [False] * (X + 1)
for b in B:
    trap[b] = True

dp = [False] * (X + 1)
dp[0] = True
for i in range(1, X + 1):
    for a in A:
        if i - a >= 0 and dp[i - a] and not trap[i]:
            dp[i] = True
            break

print("Yes" if dp[X] else "No")
