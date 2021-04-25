n = int(input())
s = input()
q = int(input())
first = list(s[:n])
latter = list(s[n:])
for i in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        if a > n:
            _a = latter[abs(n-a)-1]
            _b = latter[abs(n-b)-1]
            latter[abs(n-a)-1] = _b
            latter[abs(n-b)-1] = _a
        elif b <= n:
            _a = first[a-1]
            _b = first[b-1]
            first[a-1] = _b
            first[b-1] = _a
        elif a <= n and b > n:
            _a = first[a-1]
            _b = latter[abs(n-b)-1]
            first[a-1] = _b
            latter[abs(n-b)-1] = _a
    elif t == 2:
        tmp = first
        first = latter
        latter = tmp
print("".join(first + latter))
