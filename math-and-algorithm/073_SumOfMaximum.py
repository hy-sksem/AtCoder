N = int(input())
A = list(map(int, input().split()))

mod = 10**9 + 7
power = [0 for i in range(N)]
power[0] = 1
for i in range(1, N):
    power[i] = (2 * power[i - 1]) % mod

ans = 0
for i in range(N):
    ans += A[i] * power[i]
    ans %= mod

print(ans)
