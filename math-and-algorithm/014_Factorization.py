def factorization(n):
    l = []
    temp = n
    for i in range(2, int(-(-(n**0.5) // 1)) + 1):
        while temp % i == 0:
            temp //= i
            l.append(i)
    if temp != 1:
        l.append(temp)
    return l


N = int(input())
print(*factorization(N), " ")
