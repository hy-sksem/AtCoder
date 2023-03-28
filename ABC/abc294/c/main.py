from bisect import bisect_left

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a_idx = ""
b_idx = ""
cur = 0
pre_idx = 0
for a in A:
    idx = bisect_left(B, a)
    if idx - pre_idx == 0:
        pre_idx = idx
        cur += 1
        a_idx += str(cur) + " "
    else:
        diff = idx - pre_idx
        b_idx += " ".join([str(cur + i) for i in range(1, diff + 1)]) + " "
        cur += diff + 1
        a_idx += str(cur) + " "
        pre_idx = idx
b_idx += " ".join([str(cur + i) for i in range(1, M - pre_idx + 1)])
print(a_idx.strip())
print(b_idx.strip())
