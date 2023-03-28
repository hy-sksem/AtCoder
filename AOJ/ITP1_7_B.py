from itertools import combinations

while True:
    N, X = map(int, input().split())
    if N == 0 and X == 0:
        break
    ans = 0
    for i in combinations(range(1, N + 1), 3):
        if sum(i) == X:
            ans += 1
    print(ans)
