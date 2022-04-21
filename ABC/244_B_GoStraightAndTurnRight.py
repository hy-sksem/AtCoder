N = int(input())
T = input()

NEWS = ["N", "W", "S", "E"]
flag = "W"
p = [0, 0]

for i in range(N):
    if T[i] == "S":
        if flag == "W":
            p[0] += 1
        elif flag == "S":
            p[1] -= 1
        elif flag == "E":
            p[0] -= 1
        else:
            p[1] += 1
    else:
        flag = NEWS[(NEWS.index(flag) + 1) % 4]
print(p[0], p[1])
