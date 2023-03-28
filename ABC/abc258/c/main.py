N, Q = map(int, input().split())
S = list(input())

first_i = 0
for i in range(Q):
    q, x = map(int, input().split())
    if q == 1:
        first_i -= x
        first_i %= N
    else:
        print(S[(first_i + x - 1) % N])
