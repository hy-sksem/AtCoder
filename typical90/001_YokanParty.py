def solve(m):
    cnt, pre = 0, 0
    for i in range(N):
        if A[i] - pre >= m and L - A[i] >= m:
            cnt += 1
            pre = A[i]
    return True if cnt >= K else False


N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

left = -1
right = L + 1
while right - left > 1:
    mid = (left + right) // 2
    if solve(mid) == False:
        right = mid
    else:
        left = mid
print(left)
