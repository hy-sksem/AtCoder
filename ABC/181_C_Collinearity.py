# https://atcoder.jp/contests/abc181/tasks/abc181_c
n = int(input())
p = [list(map(int, input().split())) for i in range(n)]
   
for j in range(n):
    for k in range(j):
        for l in range(k):
            print(range(n), range(j), range(k))
            x1 = p[j][0] - p[l][0]
            x2 = p[k][0] - p[l][0]
            y1 = p[j][1] - p[l][1]
            y2 = p[k][1] - p[l][1]
            if x1*y2 == x2*y1:
                print("Yes")
                exit()
print("No")