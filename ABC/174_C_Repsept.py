# https://atcoder.jp/contests/abc174/tasks/abc174_c

k = int(input())
l = [7 % k]
for i in range(1, k):
    l.append((l[i-1] * 10 + 7) % k) 
for j in range(k):
    if l[j] == 0:
        print(j + 1)
        exit()
print(-1)