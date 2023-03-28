N, K = map(int, input().split())
A = set(map(int, input().split()))

A = sorted(list(A))
B = set(A[:K])
comp = set(range(K + 1))
print(min(comp - B))
