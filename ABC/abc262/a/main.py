Y = int(input())
mod = Y % 4
if mod <= 2:
    print(Y + abs(mod - 2))
elif mod == 3:
    print(Y + 3)
