N, K = map(int, input().split())

yojisho = 0
for a in range(1, N + 1):
    l = max(1, a - (K - 1))
    r = min(N, a + (K - 1))
    for b in range(l, r + 1):
        for c in range(l, r + 1):
            if abs(b - c) <= K - 1:
                yojisho += 1

print(N ** 3 - yojisho)
