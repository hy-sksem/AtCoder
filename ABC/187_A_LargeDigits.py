A, B = map(str, input().split())
a_sum = 0
b_sum = 0
for a in A:
    a_sum += int(a)
for b in B:
    b_sum += int(b)
print(max(a_sum, b_sum))