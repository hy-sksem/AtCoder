import collections


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

c = collections.Counter(A)

for i in range(M):
    if c[B[i]] > 0:
        c[B[i]] -= 1
    else:
        print("No")
        exit()
print("Yes")
