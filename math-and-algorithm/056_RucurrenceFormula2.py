from copy import deepcopy

MOD = 10**9 + 7


def multiply(A, B):
    C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                C[i][j] += A[i][k] * B[k][j]
                C[i][j] %= MOD
    return C


def power(A, n):
    P = deepcopy(A)
    Q = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
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
A = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]
B = power(A, N - 1)

ans = (2 * B[2][0] + B[2][1] + B[2][2]) % MOD
print(ans)
