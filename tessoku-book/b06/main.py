def solve(i, x):
    atari = x
    hazure = i - x
    if atari > hazure:
        return "win"
    elif atari == hazure:
        return "draw"
    else:
        return "lose"


N = int(input())
A = list(map(int, input().split()))
s = [0] * (N + 1)
for i in range(1, N + 1):
    s[i] = s[i - 1] + A[i - 1]

for i in range(int(input())):
    l, r = map(int, input().split())
    cnt = s[r] - s[l - 1]
    print(solve(r - l + 1, cnt))
