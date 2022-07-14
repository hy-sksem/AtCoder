N = int(input())
L, R = [0] * N, [0] * N
for i in range(N):
    L[i], R[i] = map(int, input().split())

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        cnt = 0
        for k in range(L[i], R[i] + 1):
            for l in range(L[j], R[j] + 1):
                if k > l:
                    cnt += 1
        # print("cnt", cnt, "i", i, "j", j)
        ans += cnt / ((R[i] - L[i] + 1) * (R[j] - L[j] + 1))
print(ans)
