L1, R1, L2, R2 = map(int, input().split())
d = min(R1, R2) - max(L1, L2)
print(d if d >= 0 else 0)
