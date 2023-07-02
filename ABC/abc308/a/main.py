S = list(map(int, input().split()))

_S = sorted(S)

if S == _S and 100 <= min(S) and max(S) <= 675:
    for i in range(len(S)):
        if S[i] % 25 != 0:
            exit(print("No"))
    print("Yes")
else:
    print("No")
