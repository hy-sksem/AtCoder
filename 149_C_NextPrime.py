# https://atcoder.jp/contests/abc149/tasks/abc149_c

import math
X = int(input())

def is_prime(n):
    if n == 1: return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

while True:
    if is_prime(X):
        print(X)
        exit()
    else:
        X += 1