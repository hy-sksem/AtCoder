# https://atcoder.jp/contests/abc176/tasks/abc176_a

n, x, t = map(int, input().split())
ans = -(-n // x) * t 
print(ans)