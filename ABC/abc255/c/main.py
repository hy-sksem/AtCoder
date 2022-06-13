X, A, D, N = map(int, input().split())
B = A + D * (N - 1)
if A > B:
    A, B = B, A
D = abs(D)
if D == 0:
    print(abs(X - A))
    exit()
if A <= X <= B:
    q, mod = divmod(X - A, D)
    print(min(mod, D - mod))
else:
    print(min(abs(X - A), abs(X - B)))
