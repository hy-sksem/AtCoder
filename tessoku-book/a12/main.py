def check(x):
    sum = 0
    for i in range(N):
        sum += x // A[i]
    return True if sum >= K else False


N, K = map(int, input().split())
A = list(map(int, input().split()))

l = 1
r = 10**9

while l < r:
    mid = (l + r) // 2
    if check(mid):
        r = mid
    else:
        l = mid + 1
print(l)
