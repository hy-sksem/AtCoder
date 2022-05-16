# https://atcoder.jp/contests/abc166/tasks/abc166_c

N, M = map(int, input().split())
H = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(M)]

ma = [0] * N
for i, m in enumerate(AB):
    a, b = m[0] - 1, m[1] - 1
    ma[a] = max(ma[a], H[b])
    ma[b] = max(ma[b], H[a])

ans = 0
for j in range(N):
    ans += 1 if H[j] > ma[j] else 0
print(ans)
