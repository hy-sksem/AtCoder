N = int(input())

ans = [i for i in range(1, int(N ** 0.5)+1) if N % i == 0]
for j in ans:
    if N // j == j:
        print(j)
    else:
        print(j)
        print(N // j)
print()
