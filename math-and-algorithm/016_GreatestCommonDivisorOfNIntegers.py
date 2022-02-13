def GCD(A:int, B:int) -> int:
    while A >= 1 and B >= 1:
        if A < B:
            B = B % A
        else:
            A = A % B
    if (A >= 1):
        return A
    return B

N = int(input())
A = list(map(int, input().split()))

temp = A[0]
for a in A[1:]:
    temp = GCD(temp, a)

print(temp)
