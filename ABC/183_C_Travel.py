import math
import itertools

N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]
i = list(range(N-1))
ans = 0
for ite in itertools.permutations(i):
    cnt = 0
    for j in range(N):
        if j == 0:
            cnt += T[0][ite[j]+1]
        elif j == N-1:
            cnt += T[ite[j-1]+1][0]
        else:
            cnt += T[ite[j-1]+1][ite[j]+1]
    if cnt == K:
        ans += 1
print(ans)



    
