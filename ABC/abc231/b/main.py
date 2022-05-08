from collections import Counter

N = int(input())
S = Counter([input() for _ in range(N)])
print(max(S, key=S.get))
