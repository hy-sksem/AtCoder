N = int(input())
H = list(map(int, input().split()))
ans = 0
for i in range(N - 1):
    if H[i + 1] > H[i]:
        continue
    else:
        print(H[i])
        exit()
print(H[-1])
