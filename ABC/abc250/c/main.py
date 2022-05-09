N, Q = map(int, input().split())
b = list(range(N + 1))
pos = list(range(N + 1))

for i in range(Q):
    x = int(input())
    dest = pos[x]
    if dest == N:
        dest -= 1

    b[dest], b[dest + 1] = b[dest + 1], b[dest]
    pos[b[dest]] = dest
    pos[b[dest + 1]] = dest + 1

print(*b[1:])
