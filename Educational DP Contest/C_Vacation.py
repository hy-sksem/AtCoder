N = int(input())
activity = [list(map(int, input().split())) for _ in range(N)]

h = [[0 for _ in range(3)] for _ in range(N+1)]
for i, (a, b, c) in enumerate(activity, 1):
    yesterday = h[i-1]
    today = h[i]
    today[0] = max(yesterday[1], yesterday[2]) + a
    today[1] = max(yesterday[0], yesterday[2]) + b
    today[2] = max(yesterday[0], yesterday[1]) + c

print(max(h[N]))
