# https://atcoder.jp/contests/abc177/tasks/abc177_c

n = int(input())
a = list(map(int, input().split()))

a_sum = sum(a)
ans = 0
mod = 1000000007
for i, j in enumerate(a):
    a_sum -= a[i]
    ans += j * a_sum
print(ans % mod)