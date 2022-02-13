def GCD(A:int, B:int) -> int:
    while A >= 1 and B >= 1:
        if A < B:
            B = B % A
        else:
            A = A % B
    if (A >= 1):
        return A
    return B

def LCM(A:int, B:int) -> int:
    return (A / GCD(A, B)) * B

N = int(input())
A = list(map(int, input().split()))

temp = A[0]
for a in A[1:]:
    temp = LCM(temp, a)

print(int(temp))
