from collections import deque


def to_base9(n, b):
    if n == 0:
        return "0"
    d = deque()
    while n:
        d.appendleft(str(n % b))
        n //= b
    return "".join(d)


N, K = input().split()

for i in range(int(K)):
    N = to_base9(int(N, base=8), 9).replace("8", "5")

print(N)
