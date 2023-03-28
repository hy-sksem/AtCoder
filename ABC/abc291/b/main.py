N = int(input())
X = list(map(int, input().split()))

X = sorted(X)
print(sum(X[N:-N]) / (3 * N))
