# 問題文
# 高橋くんは今、白い服を着ています。
# 高橋くんは、白い服を着た次の日には黒い服を、黒い服を着た次の日には白い服を着ます。
# N日後には何色の服を着るでしょうか？
# 制約
# N
#  は整数である
# 1 ≤ N ≤ 30

n = int(input())
if n % 2 == 0:
    print("White")
else:
    print("Black")