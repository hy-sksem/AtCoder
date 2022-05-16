n = int(input())
a = list(map(int, input().split()))
x = int(input())

sum = 0
sum_l = []

for i in range(n):
    sum += a[i]
    sum_l.append(sum)
    if sum > x:
        print(i + 1)
        exit()

q, x = divmod(x, sum)
for j in range(len(sum_l)):
    temp = x - sum_l[j]
    if temp < 0:
        print(n * q + j + 1)
        exit()
