from copy import deepcopy

MOD = 10**9


def multiply(A, B):
    C = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] += A[i][k] * B[k][j]
                C[i][j] %= MOD
    return C


def power(A, n):
    P = deepcopy(A)
    Q = [[0, 0], [0, 0]]
    flag = False
    for i in range(60):
        if n & (1 << i):
            if not flag:
                Q = deepcopy(P)
                flag = True
            else:
                Q = deepcopy(multiply(Q, P))
        P = deepcopy(multiply(P, P))
    return Q


N = int(input())
A = [[1, 1], [1, 0]]
B = power(A, N - 1)

ans = (B[1][0] + B[1][1]) % MOD
print(ans)
