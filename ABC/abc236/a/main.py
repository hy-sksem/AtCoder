S = input()
a, b = map(int, input().split())
a -= 1
b -= 1

ta, tb = S[b], S[a]
index_a = a + 1
index_b = b + 1
print(S[:a] + ta + S[index_a:b] + tb + S[index_b:])
