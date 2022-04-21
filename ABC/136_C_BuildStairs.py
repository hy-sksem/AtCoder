# https://atcoder.jp/contests/abc136/tasks/abc136_c

N = int(input())
H = list(map(int, input().split()))

f = H[0]
for h in H:
    if f <= h-1:
        f = h-1
    elif f <= h:
        f = h
    else:
        print("No")
        exit()
print("Yes")