N = int(input())
q, r = divmod(N, 5)
print(q * 5 if r <= 2 else (q + 1) * 5)
