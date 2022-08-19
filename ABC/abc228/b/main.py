def int1(x: int) -> int:
    return int(x) - 1


N, X = map(int, input().split())
A = list(map(int1, input().split()))

b = [False] * N
X -= 1
while not b[X]:
    b[X] = True
    X = A[X]
print(sum(b))
