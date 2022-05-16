X, Y = map(int, input().split())

print(0 if X >= Y else (Y - X + 9) // 10)
