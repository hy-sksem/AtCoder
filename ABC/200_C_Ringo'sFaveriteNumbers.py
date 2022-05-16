n = int(input())
a = list(map(int, input().split()))
b = [0] * 200
for i in a:
    b[i % 200] += 1
ans = 0
for j in b:
    ans += (j * (j - 1)) / 2
print(int(ans))
