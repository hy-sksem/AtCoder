N = int(input())
P = list(map(int, input().split()))

p = P[-1]
cnt = 1
while True:
    if p == 1:
        break
    p = P[p - 2]
    cnt += 1
print(cnt)
