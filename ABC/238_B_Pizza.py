N = int(input())
A = list(map(int, input().split()))

D = [False] * 360
D[0] = True

index = 0
for a in A:
    index = index + a if index + a <= 359 else index + a - 360
    D[index] = True

D = [i for i, x in enumerate(D) if x]
D.append(360)
ans = 0
for i in range(len(D) - 1):
    ans = D[i + 1] - D[i] if D[i + 1] - D[i] >= ans else ans
print(ans)
