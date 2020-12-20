# https://atcoder.jp/contests/abc175/tasks/abc175_b

n = int(input())
l = list(map(int, input().split()))

ans = 0
for i in l:
    for j in l:
        for k in l:
            h = [i, j, k]
            if i != j and i != k and j != k:
                h.sort()
                if h[0] + h[1] > h[2]:
                    ans += 1
print(ans // 6)
