N = int(input())
A = list(map(int, input().split()))

perf = list(range(1, N + 1))
print((sum(perf)) * 4 - sum(A))
