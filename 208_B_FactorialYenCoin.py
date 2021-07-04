import math

def fact(tgt, num, ans):
    if num == 1:
        ans += tgt
        return ans
    ans += (r := tgt // math.factorial(num))
    tgt -= r * math.factorial(num)
    return fact(tgt, num-1, ans)

p = int(input())
print(fact(p, 10, 0))