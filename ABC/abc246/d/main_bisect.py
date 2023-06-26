N = int(input())


def calc(a, b):
    return a**3 + a**2 * b + a * b**2 + b**3


ans = 10**18
for i in range(10**6):
    ng, ok = -1, 10**6
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if calc(i, mid) >= N:
            ok = mid
        else:
            ng = mid
    ans = min(ans, calc(i, ok))
print(ans)
