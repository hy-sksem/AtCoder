N, K = map(int, input().split())
S = [input() for _ in range(N)]

for s in sorted(S[:K]):
    print(s)
