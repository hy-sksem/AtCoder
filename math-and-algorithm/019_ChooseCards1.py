N = int(input())
A = list(map(int, input().split()))

cnt = [0] * 4
for a in A:
    cnt[a] += 1

print(
    int(
        cnt[1] * (cnt[1] - 1) / 2
        + cnt[2] * (cnt[2] - 1) / 2
        + cnt[3] * (cnt[3] - 1) / 2
    )
)
