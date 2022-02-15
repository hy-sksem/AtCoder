N = int(input())
A = list(map(int, input().split()))

cnt = [0]*4
for a in A:
    cnt[a//100 - 1] += 1

print(cnt[0]*cnt[3] + cnt[1]*cnt[2])
