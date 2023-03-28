N = int(input())
P = list(map(int, input().split()))
for i in range(N - 2, -1, -1):
    p = P[i:]
    if p[0] > p[1]:
        _p = sorted(p, reverse=True)
        head = _p[_p.index(p[0]) + 1]
        _p.remove(head)
        tmp = [head] + _p
        ans = P[:i] + tmp
        print(*ans)
        exit()
