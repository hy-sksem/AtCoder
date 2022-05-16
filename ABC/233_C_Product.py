N, X = map(int, input().split())
DP = {1: 1}

for i in range(N):
    A = list(map(int, input().split()))
    NDP = dict()

    for dp in DP:
        for a in A[1:]:
            if dp * a in NDP:
                NDP[dp * a] += DP[dp]
            else:
                NDP[dp * a] = DP[dp]
    DP = NDP
print(DP[X] if X in DP else 0)
