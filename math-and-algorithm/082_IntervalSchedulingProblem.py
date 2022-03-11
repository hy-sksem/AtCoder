N = int(input())
A = []
for i in range(N):
    a, b = map(int, input().split())
    A.append([b, a])

A.sort()

current_time = 0
ans = 0
for i in range(N):
    if current_time <= A[i][1]:
        current_time = A[i][0]
        ans += 1

print(ans)
