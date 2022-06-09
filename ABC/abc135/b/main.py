# https://atcoder.jp/contests/abc135/tasks/abc135_b

N = int(input())
P = list(map(int, input().split()))

cnt = 0
for i, p in enumerate(P):
    if p != i + 1:
        cnt += 1

print("YES" if cnt <= 2 else "NO")
