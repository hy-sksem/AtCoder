import math

S = input()
S_s = set(S)
print(int(math.factorial(len(S)) / math.factorial(len(S) - len(S_s) + 1)))
