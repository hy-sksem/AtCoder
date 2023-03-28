import math

N = int(input())
a = list(map(int, input().split()))
a_sort = sorted(a)
ans = 0
correct = 0
for i in range(N):
    if a[i] == i + 1:
        correct += 1
    elif min(a[i], a[a[i] - 1]) == i + 1 and max(a[i], a[a[i] - 1]) == a[i]:
        ans += 1
print(ans + math.comb(correct, 2))
