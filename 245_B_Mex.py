N = int(input())
A = set(map(int, input().split()))

s = set(range(N + 1))
print(min(s - A))
