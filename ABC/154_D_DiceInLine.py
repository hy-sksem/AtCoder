# https://atcoder.jp/contests/abc154/tasks/abc154_d

N, K = map(int, input().split())
P = list(map(int, input().split()))

f = 0
for i in range(K):
    f += P[i]
ans = f
for j in range(K, N):
    d = P[j] - P[j-K]
    if d > 0:
        f += d
        if f > ans:
            ans = f
    else:
        f += d
print((ans+K)/2)
