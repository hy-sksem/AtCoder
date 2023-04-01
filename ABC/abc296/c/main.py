N, X = map(int, input().split())
A = set(map(int, input().split()))
_A = A.copy()
while A:
    a = A.pop()
    if X + a in _A:
        exit(print("Yes"))
    elif X == a - a:
        exit(print("Yes"))
print("No")
