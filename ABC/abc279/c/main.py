from collections import defaultdict

H, W = map(int, input().split())
S = [input() for _ in range(H)]
T = [input() for _ in range(H)]
ds = defaultdict(int)
dt = defaultdict(int)

for w in range(W):
    hash_s = []
    hash_t = []
    for h in range(H):
        if S[h][w] == "#":
            hash_s.append(h)
        if T[h][w] == "#":
            hash_t.append(h)
    ds[tuple(hash_s)] += 1
    dt[tuple(hash_t)] += 1

# print(ds)
# print(dt)
print("Yes" if ds == dt else "No")
