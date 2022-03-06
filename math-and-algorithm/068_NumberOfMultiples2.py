def GCD(A, B):
    while A >= 1 and B >= 1:
        if A > B:
            A %= B
        else:
            B %= A
    if A >= 1:
        return A
    return B


def LCM(A, B):
    return int(A // GCD(A, B)) * B


N, K = map(int, input().split())
V = list(map(int, input().split()))

ans = 0
for i in range(1, 1 << K):
    cnt = 0
    lcm = 1
    for j in range(K):
        if i & (1 << j):
            cnt += 1
            lcm = LCM(lcm, V[j])

    num = N // lcm
    if cnt % 2 == 1:
        ans += num
    else:
        ans -= num

print(ans)
