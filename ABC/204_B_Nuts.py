n = int(input())
a = list(map(int, input().split()))
cnt = 0
for i in a:
    if i <= 10:
        continue
    else:
        cnt += i-10
print(cnt)
