x1, y1, x2, y2 = map(int, input().split())

m = []
n = []

m.append([x1 + 2, y1 + 1])
m.append([x1 + 2, y1 - 1])
m.append([x1 + 1, y1 + 2])
m.append([x1 + 1, y1 - 2])
m.append([x1 - 1, y1 + 2])
m.append([x1 - 1, y1 - 2])
m.append([x1 - 2, y1 + 1])
m.append([x1 - 2, y1 - 1])

n.append([x2 + 1, y2 + 2])
n.append([x2 + 1, y2 - 2])
n.append([x2 - 1, y2 + 2])
n.append([x2 - 1, y2 - 2])
n.append([x2 + 2, y2 + 1])
n.append([x2 + 2, y2 - 1])
n.append([x2 - 2, y2 + 1])
n.append([x2 - 2, y2 - 1])

for i in m:
    if i in n:
        print("Yes")
        exit()
print("No")
