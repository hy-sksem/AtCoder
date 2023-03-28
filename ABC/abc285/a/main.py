a, b = map(int, input().split())
print("Yes" if max(a, b) // 2 == min(a, b) else "No")
