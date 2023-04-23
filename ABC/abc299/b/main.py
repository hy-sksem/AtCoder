N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

ans = 0
if T not in C:
    T = C[0]
    ans = 1
tmp = 0
for i, c in enumerate(C, start=1):
    if c == T and R[i - 1] > tmp:
        ans = i
        tmp = R[i - 1]

print(ans)
