# https://atcoder.jp/contests/abc145/tasks/abc145_b

N = int(input())
S = input()

first_h = S[: N // 2]
second_h = S[N // 2 :]
print("Yes" if first_h == second_h else "No")
