from itertools import combinations

H1, W1 = map(int, input().split())
A1 = [list(input().split()) for _ in range(H1)]
H2, W2 = map(int, input().split())
A2 = [list(input().split()) for _ in range(H2)]

for i in combinations(range(H1), H2):  # 残す行の組み合わせ
    for j in combinations(range(W1), W2):  # 残す列の組み合わせ
        tmp = [[-1] * W2 for _ in range(H2)]
        for h_i, k in enumerate(i):
            for w_i, l in enumerate(j):
                tmp[h_i][w_i] = A1[k][l]
        if tmp == A2:
            print("Yes")
            exit()
print("No")
