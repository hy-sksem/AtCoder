N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(sum(A)*(1/3) + sum(B)*(2/3))
