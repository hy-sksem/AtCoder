N, K = map(int, input().split())
A = list(map(int, input().split()))

first = A[: N // 2]
second = A[N // 2 :]
sum1 = []
for i in range(1 << len(first)):
    sum = 0
    for j in range(len(first)):
        if (i >> j) & 1:
            sum += first[j]
    sum1.append(sum)

sum2 = []
for i in range(1 << len(second)):
    sum = 0
    for j in range(len(second)):
        if (i >> j) & 1:
            sum += second[j]
    sum2.append(sum)

sum1 = sorted(sum1)
sum2 = sorted(sum2)
cnt = 0
for s in sum1:
    x = K - s
    l, r = 0, len(sum2) - 1
    for _ in range(2**4):
        mid = (l + r + 1) // 2
        if x < sum2[mid]:
            r = mid
        else:
            l = mid
    if x == sum2[l] or x == sum2[r]:
        cnt += 1
print("Yes" if cnt else "No")
