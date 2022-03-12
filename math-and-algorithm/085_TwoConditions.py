N, X, Y = map(int, input().split())

for i in range(1, N + 1):
    for j in range(i, N + 1):
        for k in range(j, N + 1):
            for l in range(k, N + 1):
                if i + j + k + l == X and i * j * k * l == Y:
                    print("Yes")
                    exit()
print("No")
