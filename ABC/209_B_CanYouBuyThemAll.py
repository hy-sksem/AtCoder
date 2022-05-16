n, x = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
for i, j in enumerate(a, start=1):
    if i % 2 == 0:
        cnt += j - 1
    else:
        cnt += j
    if cnt > x:
        print("No")
        exit()
print("Yes")
