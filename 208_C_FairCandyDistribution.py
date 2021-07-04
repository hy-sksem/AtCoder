n, k = map(int, input().split())
a = list(map(int, input().split()))
a_sorted = sorted(a)

d = a_sorted[k%n-1] if k % n != 0 else 0
for i in a:
    if i <= d:
        print(k//n+1)
    else:
        print(k//n)
