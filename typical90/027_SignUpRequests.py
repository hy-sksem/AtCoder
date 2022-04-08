N = int(input())
user = set()

for i in range(1, N + 1):
    s = input()
    if s in user:
        continue
    else:
        user.add(s)
        print(i)
