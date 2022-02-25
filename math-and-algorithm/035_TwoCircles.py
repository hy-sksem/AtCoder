x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())

def distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

if distance(x1, y1, x2, y2) < abs(r1-r2):
    print(1)
elif distance(x1, y1, x2, y2) == abs(r1-r2):
    print(2)
elif distance(x1, y1, x2, y2) < r1+r2:
    print(3)
elif distance(x1, y1, x2, y2) == r1+r2:
    print(4)
else:
    print(5)
