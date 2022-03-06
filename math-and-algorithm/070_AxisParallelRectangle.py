def check_numpoints(N, X, Y, lx, rx, ly, ry):
    cnt = 0
    for i in range(N):
        if lx <= X[i] <= rx and ly <= Y[i] <= ry:
            cnt += 1
    return cnt


N, K = map(int, input().split())
X = [None] * N
Y = [None] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())

ans = 10**19

for i in range(N):
    for j in range(N):
        for k in range(N):
            for l in range(N):
                cl, cr, dl, dr = X[i], X[j], Y[k], Y[l]
                if cl < cr and dl < dr:
                    if check_numpoints(N, X, Y, cl, cr, dl, dr) >= K:
                        area = (cr - cl) * (dr - dl)
                        ans = min(ans, area)

print(ans)
