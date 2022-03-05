N = int(input())

flag = False
for i in range(1, 60):
    if N == (2**i) - 1:
        flag = True
        break
print("Second" if flag else "First")
