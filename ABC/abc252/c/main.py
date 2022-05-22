def add(x):
    if x in temp:
        return add(x + 10)
    return temp.append(x)


N = int(input())
S = [input() for _ in range(N)]
cnt = []

for i in range(10):
    temp = []
    for j in range(N):
        index = S[j].find(str(i))
        add(index)
    cnt.append(max(temp))

print(min(cnt))
