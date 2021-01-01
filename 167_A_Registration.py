# https://atcoder.jp/contests/abc167/tasks/abc167_a

S = input()
T = input()
print("Yes") if S == T[0:len(S)] and len(T) - 1 == len(S) else print("No")