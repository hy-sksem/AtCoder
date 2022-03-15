a, b, c = map(int, input().split())

if c == 1:
    print("No")
    exit()

v = c**0
for i in range(b):
    v *= c
    if a < v:
        print("Yes")
        exit()
print("No")
