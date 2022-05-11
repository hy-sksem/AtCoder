S = input()
a, b = map(int, input().split())
a -= 1
b -= 1

ta, tb = S[b], S[a]
print(S[:a] + ta + S[a + 1 : b] + tb + S[b + 1 :])
