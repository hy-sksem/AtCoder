def int1(x: int) -> int:
    return int(x) - 1


N, K, Q = map(int, input().split())
A = list(map(int1, input().split()))
L = list(map(int1, input().split()))
df = [0 for _ in range(N)]
for a in A:
    df[a] = 1
for i in range(Q):
    l = L[i]
    if A[l] + 1 >= N or df[A[l] + 1] == 1:
        continue
    df[A[l]], df[A[l] + 1] = df[A[l] + 1], df[A[l]]
    A[l] += 1
ans = []
for i in range(N):
    if df[i] == 1:
        ans.append(i + 1)
print(*ans)
