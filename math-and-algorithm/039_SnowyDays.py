N, Q = map(int, input().split())
D = [0] * (N+2)
for i in range(Q):
    L, R, X = map(int, input().split())
    D[L] += X
    D[R+1] -= X
ans = []
for d in D[2:-1]:
    if d < 0:
        ans.append(">")
    elif d > 0:
        ans.append("<")
    else:
        ans.append("=")
print(*ans, sep="")
