# https://atcoder.jp/contests/abc143/tasks/abc143_b

N = int(input())
d = list(map(int, input().split()))

t = 0
for i in range(N):
    for j in range(i+1, N):
        t += d[i]*d[j]
print(t)        