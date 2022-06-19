h1, h2, h3, w1, w2, w3 = map(int, input().split())

ans = 0
for i in range(1, h1):
    for j in range(1, h1):
        h1_3 = h1 - i - j
        if h1_3 <= 0:
            continue
        for k in range(1, h2):
            for l in range(1, h2):
                h2_3 = h2 - k - l
                if h2_3 <= 0:
                    continue
                h3_1 = w1 - i - k
                h3_2 = w2 - j - l
                h3_3 = w3 - h1_3 - h2_3
                if h3_1 <= 0 or h3_2 <= 0 or h3_3 <= 0:
                    continue
                if h3_1 + h3_2 + h3_3 == h3:
                    ans += 1

print(ans)
