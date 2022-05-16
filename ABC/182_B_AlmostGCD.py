# https://atcoder.jp/contests/abc182/tasks/abc182_b

N = int(input())
A = list(map(int, input().split()))

max_gcd = 0
ans = 0
for i in range(2, max(A) + 1):
    cnt = 0
    for a in A:
        if a % i == 0:
            cnt += 1
    if max_gcd < cnt:
        max_gcd = cnt
        ans = i

print(ans)
