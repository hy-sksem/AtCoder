A = []
while True:
    a = int(input())
    A.append(a)
    if a == 0:
        break
A.reverse()
for a in A:
    print(a)
