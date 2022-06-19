N = int(input())
df = [0 for _ in range(2 * 10**5 + 1)]
for i in range(N):
    L, R = map(int, input().split())
    df[L] += 1
    df[R] -= 1

cnt = 0
start = 0
for i in range(2 * 10**5 + 1):
    if df[i] == 0 and cnt:
        continue
    if df[i] > 0:
        if cnt == 0:
            start = i
        cnt += df[i]
    if df[i] < 0:
        cnt += df[i]
        if cnt == 0:
            print(start, i)
