N, M, X, T, D = map(int, input().split())
if X <= M <= N:
    print(T)
else:
    print(T - (X - M) * D)
