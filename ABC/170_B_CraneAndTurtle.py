# https://atcoder.jp/contests/abc170/tasks/abc170_b

x, y = map(int, input().split())

for i in range(x, -1, -1):
    if i * 4 + (x - i) * 2 == y:
        print("Yes")
        exit()
    elif i * 4 + (x - i) * 2 > y:
        continue
print("No")
