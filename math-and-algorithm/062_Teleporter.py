N, K = map(int, input().split())
A = list(map(int, input().split()))

First = [-1 for i in range(N + 1)]
Second = [-1 for i in range(N + 1)]

cnt = 0
cur = 1
while True:
    if First[cur] == -1:
        First[cur] = cnt
    elif Second[cur] == -1:
        Second[cur] = cnt

    if cnt == K:
        print(cur)
        exit()
    elif Second[cur] != -1 and (K - First[cur]) % (Second[cur] - First[cur]) == 0:
        print(cur)
        exit()
    cur = A[cur - 1]
    cnt += 1
