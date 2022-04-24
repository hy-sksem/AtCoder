N, K = map(int, input().split())
S = [input() for _ in range(N)]
ans = 0

for i in range(1 << N):
    c = [0] * 26
    for j in range(N):
        if i >> j & 1:
            for k in S[j]:
                c[ord(k) - ord("a")] += 1
    ans = max(ans, c.count(K))
print(ans)
