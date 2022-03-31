N = int(input())
C = [None] * (N + 1)
P = [None] * (N + 1)
for i in range(1, N + 1):
    C[i], P[i] = map(int, input().split())

cumulative_sum1 = [0]
cumulative_sum2 = [0]

for i in range(1, N + 1):
    if C[i] == 1:
        if len(cumulative_sum1) > 0:
            cumulative_sum1.append(cumulative_sum1[-1] + P[i])
        else:
            cumulative_sum1.append(P[i])
        cumulative_sum2.append(cumulative_sum2[-1] if len(cumulative_sum2) > 0 else 0)
    else:
        if len(cumulative_sum2) > 0:
            cumulative_sum2.append(cumulative_sum2[-1] + P[i])
        else:
            cumulative_sum2.append(P[i])
        cumulative_sum1.append(cumulative_sum1[-1] if len(cumulative_sum1) > 0 else 0)
Q = int(input())
ans = []
for i in range(Q):
    L, R = map(int, input().split())
    L -= 1
    temp = []
    if len(cumulative_sum1) > 0:
        temp.append(cumulative_sum1[R] - cumulative_sum1[L])
    else:
        temp.append(0)
    if len(cumulative_sum2) > 0:
        temp.append(cumulative_sum2[R] - cumulative_sum2[L])
    else:
        temp.append(0)
    ans.append(temp)

for i in ans:
    print(*i)
