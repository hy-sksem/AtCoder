N, K, X = map(int, input().split())
A = sorted(list(map(int, input().split())), reverse=True)

goukei = sum(A)
amari = []
coupon = 0
for i in range(N):
    q, mod = divmod(A[i], X)
    if coupon + q > K:
        print(goukei - K * X)
        exit()
    coupon += q
    amari.append(mod)

amari = sorted(amari, reverse=True)
print(goukei - coupon * X - sum(amari[0 : K - coupon]))
