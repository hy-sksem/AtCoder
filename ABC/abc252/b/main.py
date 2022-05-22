def int1(x: int) -> int:
    return int(x) - 1


N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int1, input().split()))

m = max(A)

for i in range(K):
    if A[B[i]] == m:
        print("Yes")
        exit()
print("No")
