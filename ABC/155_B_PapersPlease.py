# https://atcoder.jp/contests/abc155/tasks/abc155_b

N = int(input())
A = list(map(int, input().split()))
ans = "APPROVED"

for a in A:
    if a % 2 == 0:
        if a % 3 == 0 or a % 5 == 0:
            continue
        else:
            ans = "DENIED"
            print(ans)
            exit()
print(ans)
