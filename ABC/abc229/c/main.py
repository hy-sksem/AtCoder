N, W = map(int, input().split())
AB = [0] * N

for i in range(N):
    AB[i] = list(map(int, input().split()))
AB.sort(key=lambda x: x[0], reverse=True)

ans = 0
i = 0
while W > 0:
    if i >= N:
        break
    for j in range(AB[i][1]):
        ans += AB[i][0]
        W -= 1
        if W == 0:
            break
    i += 1
print(ans)
