# https://atcoder.jp/contests/abc160/tasks/abc160_b

X = int(input())
print((X // 500)*1000 + ((X % 500) // 5)*5)