# https://atcoder.jp/contests/abc179/tasks/

n = int(input())
cnt = 0
for i in range(1, n):
    cnt += (n -1) // i
print(cnt)