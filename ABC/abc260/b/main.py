from collections import defaultdict

N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_d = defaultdict(list)
B_d = defaultdict(list)
sum_d = defaultdict(list)
for i in range(N):
    a = A[i]
    b = B[i]
    A_d[a].append(i)
    B_d[b].append(i)
    sum_d[a + b].append(i)

A_d = sorted(A_d.items(), key=lambda x: x[0], reverse=True)
B_d = sorted(B_d.items(), key=lambda x: x[0], reverse=True)
sum_d = sorted(sum_d.items(), key=lambda x: x[0], reverse=True)

ans = list()

for k, v in A_d:
    for i in v:
        if X == 0:
            break
        ans.append(i)
        X -= 1
for k, v in B_d:
    for i in v:
        if i in ans:
            continue
        if Y == 0:
            break
        ans.append(i)
        Y -= 1

for k, v in sum_d:
    for i in v:
        if i in ans:
            continue
        if Z == 0:
            break
        ans.append(i)
        Z -= 1

for a in sorted(ans):
    print(a + 1)
