A, B = input().split()

ans = "Easy"
for a, b in zip(reversed(A), reversed(B)):
    if int(a) + int(b) >= 10:
        ans = "Hard"
print(ans)
