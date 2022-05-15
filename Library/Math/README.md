# 整数問題系

1. 素数判定

   ```python
   def isprime(N) -> bool:
       if N < 2:
           return False
       i = 2
       while i * i <= N:
           if N % i == 0:
               return False
           i += 1
       return True
   ```

2. エラトステネスの篩

    計算量: O(NloglogN)

   ```python
   def Eratosthenes(N:int) -> list[bool]:
       isprime = [True] * (N+1)
       isprime[0], isprime[1] = False, False

       for p in range(2, N+1):
           if not isprime[p]:
               continue

           q = p * 2
           while q <= N:
               isprime[q] = False
               q += p

       return isprime
   ```

   ```python

   def Eratosthenes(N:int) -> list[int]:
    isprime = [True] * (N + 1)
    isprime[0], isprime[1] = False, False
    primes = []
    for p in range(2, N + 1):
        if not isprime[p]:
            continue
        primes.append(p)

        q = p * 2
        while q <= N:
            isprime[q] = False
            q += p

    return primes
    ```

3. 約数全列挙

   ```python
   # N の約数をすべて求める関数
   def calc_divisors(N) -> list(int):
       res = []

       for i in range(1, N + 1):
           if i * i > N:
               break

           if N % i != 0:
               continue

           res.append(i)

           if N // i != i:
               res.append(N // i)

       res.sort()
       return res
   ```

4. 倍数の性質

    ```txt
    - 2の倍数: 1の位が2の倍数
    - 3の倍数: 各桁の和が3の倍数
    - 4の倍数: 下2桁が4の倍数
    - 5の倍数: 1の位が5の倍数
    - 8の倍数: 下3桁が8の倍数
    - 9の倍数: 各桁の和が9の倍数
    - 11の倍数: (奇数桁目の数字の和) - (偶数桁目の数字の和)が11の倍数
    ```