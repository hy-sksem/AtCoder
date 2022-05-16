L, R = map(int, input().split())
S = [i for i in input()]

L -= 1

S = S[:L] + list(reversed(S[L:R])) + S[R:]
print("".join(S))
