# 概要
AtCoderの問題を解く

▼以下は自分用メモ
## 動的計画法

1. 1次元（フィボナッチ数列）
    ```python
    N = int(input())

    # 初期化
    F = [0] * (N+1)

    # 初期値
    F[0], F[1] = 1, 1

    for i in range(2, N+1):
        F[i] = F[i-2] + F[i-1]
    print(F[N]) 
    ```

1. 2次元（道順 左上 -> 右下）
    ```python
    N = int(input())

    # 2次元配列の初期化
    dp = [[0] * N for _ in range(N)]

    # 初期値
    dp[0][0] = 1

    for i in range(N):
        for j in range(N):
            # 上から
            if i - 1 >= 0:
                dp[i][j] += dp[i-1][j]

            # 左から
            if j - 1 >= 0:
                dp[i][j] += dp[i][j-1]

    print(dp[N-1][N-1])
    ```
