a, b = map(int, input().split())

if abs(a-b) == 1:
    print("Yes")
elif min(a,b) == 1 and max(a,b) == 10:
    print("Yes")
else:
    print("No")
    