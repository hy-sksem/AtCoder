N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

F = [["."] * (S - R + 1) for _ in range(Q - P + 1)]

for i in range(Q - P + 1):
    for j in range(S - R + 1):
        x = i + P
        y = j + R

        if abs(x - A) == abs(y - B):
            F[i][j] = "#"

for f in F:
    print("".join(f))
