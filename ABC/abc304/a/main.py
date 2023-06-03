N = int(input())
SA = [input().split() for _ in range(N)]

min_i = 0
minimum = 10**9
for i in range(N):
    if int(SA[i][1]) < minimum:
        minimum = int(SA[i][1])
        min_i = i
for i in list(range(min_i, N)) + list(range(0, min_i)):
    print(SA[i][0])
