# https://atcoder.jp/contests/abc156/tasks/abc156_a

N, R = map(int, input().split())
print(R) if N >= 10 else print(R + (100 * (10 - N)))
