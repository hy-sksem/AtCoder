H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

for i in range(1, H+1):
    for j in range(i+1, H+1):
        for k in range(1, W+1):
            for l in range(k+1, W+1):
                if A[i-1][k-1] + A[j-1][l-1] > A[j-1][k-1] + A[i-1][l-1]:
                    print("No")
                    exit()
print("Yes")