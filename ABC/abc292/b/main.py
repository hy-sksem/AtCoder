N, Q = map(int, input().split())
yellew_card = [0] * N
red_card = [0] * N

for _ in range(Q):
    q, x = map(int, input().split())
    if q == 1:
        yellew_card[x - 1] += 1
    elif q == 2:
        red_card[x - 1] += 1
    elif q == 3:
        print("Yes" if yellew_card[x - 1] >= 2 or red_card[x - 1] >= 1 else "No")
