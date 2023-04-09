A, B = map(int, input().split())

ans = 0
while A != B:
    if A > B:
        diff = A - B
        x = diff // B
        A -= x * B
        ans += x
        if A > B:
            A -= B
            ans += 1
    else:
        diff = B - A
        x = diff // A
        B -= x * A
        ans += x
        if B > A:
            B -= A
            ans += 1

print(ans)
