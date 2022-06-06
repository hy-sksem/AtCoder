from bisect import bisect_right

N = int(input())
square_num = [i * i for i in range(1, 2 * N)]
d = list(range(N + 1))
for i in range(2, N + 1):
    i *= i
    # 平方数となる最小の値を探す
    for j in range(i, N + 1, i):
        while d[j] % i == 0:
            d[j] //= i  # 平方数で割った値を残す

print(d, square_num)
ans = 0
for i in range(1, N + 1):
    # i*jが平方数となるj、つまりd[i]*jが平方数となる1以上N以下の整数jの個数はjが平方数となる1以上N/d[i]以下の整数jの個数と一致
    ans += bisect_right(square_num, N // d[i])
print(ans)
