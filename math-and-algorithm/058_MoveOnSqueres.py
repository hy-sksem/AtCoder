N, X, Y = map(int, input().split())

print("Yes" if (X + Y) % 2 == N % 2 and abs(X + Y) <= N else "No")
