# https://atcoder.jp/contests/abc189/tasks/abc189_c

N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    min_a = A[i]
    cnt = 0
    for j in range(i, N):
        min_a = min(min_a, A[j])
        cnt = max(cnt, min_a * (j - i + 1))
    ans = max(ans, cnt)
print(ans)
