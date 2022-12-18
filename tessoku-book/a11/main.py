N, X = map(int, input().split())
A = list(map(int, input().split()))

l = 0
r = N - 1
while l <= r:
    mid = (r + l) // 2
    if A[mid] == X:
        exit(print(mid + 1))
    elif A[mid] > X:
        r = mid - 1
    else:
        l = mid + 1
