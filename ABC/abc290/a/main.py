N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = 0
for b in B:
    cnt += A[b - 1]
print(cnt)
