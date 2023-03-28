from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))

srt_A = sorted(list(set(A)))
B = []
for a in A:
    idx = bisect_left(srt_A, a)
    B.append(idx + 1)

print(*B)
