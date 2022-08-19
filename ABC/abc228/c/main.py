N, K = map(int, input().split())

s = [0] * N
for i in range(N):
    s[i] = sum(map(int, input().split()))

k = sorted(s, reverse=True)[K - 1]
for i in range(N):
    print("Yes" if s[i] + 300 >= k else "No")
