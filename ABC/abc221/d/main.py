N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

e = []
for A, B in AB:
    e.append((A, 1))
    e.append((A + B, -1))

e.sort(key=lambda x: x[0])
print(e)
crr = 0
cnt = 0
ans = [0] * (N + 1)
for day, c in e:
    period = day - crr
    crr = day
    ans[cnt] += period
    cnt += c
print(*ans[1:])
