A, B, C = map(int, input().split())

if C == 0:
    while True:
        A -= 1
        if A <= 0:
            print("Aoki")
            exit()
        B -= 1
        if B <= 0:
            print("Takahashi")
            exit()
else:
    while True:
        B -= 1
        if B <= 0:
            print("Takahashi")
            exit()
        A -= 1
        if A <= 0:
            print("Aoki")
            exit()
