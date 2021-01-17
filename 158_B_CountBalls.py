# https://atcoder.jp/contests/abc158/tasks/abc158_b

N, A, B = map(int, input().split())
q, mod = divmod(N, A+B)
print(q*A + min(mod, A))


