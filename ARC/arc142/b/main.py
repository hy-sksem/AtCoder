N = int(input())
df = [[] for _ in range(N)]

row = 0
for i in range(1, N * N - N + 2, N):
    for j in range(N):
        # print("i:", i, "j:", j)
        df[row].append(i + j)
    if row + 2 <= N - 1:
        row += 2
    else:
        row = 1

for i in range(N):
    print(*df[i])
