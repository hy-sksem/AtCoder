# https://atcoder.jp/contests/abc165/tasks/abc165_a

K = int(input())
A, B = map(int, input().split())
print("OK") if (A // K + 1) * K <= B or A % K == 0 else print("NG")
