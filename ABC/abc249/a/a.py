A, B, C, D, E, F, X = map(int, input().split())

Takahashi = ([B] * A + [0] * C) * X
Aoki = ([E] * D + [0] * F) * X

total_t = 0
total_a = 0
for i in range(X):
    total_t += Takahashi[i]
    total_a += Aoki[i]

if total_t > total_a:
    print("Takahashi")
elif total_t < total_a:
    print("Aoki")
else:
    print("Draw")
