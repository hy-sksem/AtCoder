N = int(input())
l, r = 0, 100
while r - l > 0.001:
    mid = (l + r) / 2
    f = mid**3 + mid
    if f == N:
        exit(print(mid))
    if f < N:
        l = mid
    else:
        r = mid

print(f"{mid:.4f}")
