# 問題文
# 何も書かれていない黒板があります。 高橋くんは
# N回の操作を行い、黒板に整数を書きます。

# i回目の操作では、
# Ai 以上Bi 以下の整数すべてを1個ずつ、合計Bi−Ai+ 1個の整数を書きます。

# N回の操作を終えたときの、黒板に書かれた整数の合計を求めてください。

# 制約
# 入力はすべて整数
# 1≤N≤105
# 1≤Ai≤Bi≤106
# 入力
# 入力は以下の形式で標準入力から与えられる。

# N
# A1 B1
# ⋮
# AN BN

# 出力
# N回の操作を終えたときの、黒板に書かれた整数の合計を出力せよ。

n = int(input())
sum = 0
for i in range(n):
    a, b = map(int, input().split())
    sum += (a + b) * (b - a + 1) / 2
print(round(sum))
