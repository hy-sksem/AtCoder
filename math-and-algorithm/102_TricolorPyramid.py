def ncr(n, r):
    if n < 3 and r < 3:
        A = [[1, 0, 0], [1, 1, 0], [1, 2, 1]]
        return A[n][r]
    return ncr(n // 3, r // 3) * ncr(n % 3, r % 3) % 3


N = int(input())
C = input()

ans = 0
for i in range(N):
    code = "BWR".find(C[i])
    ans += code * ncr(N - 1, i)
    ans %= 3

if N % 2 == 0:
    ans = (3 - ans) % 3

print("BWR"[ans])
