N, X = map(int, input().split())
P = list(map(int, input().split()))

for i, p in enumerate(P, start=1):
    if p == X:
        exit(print(i))
