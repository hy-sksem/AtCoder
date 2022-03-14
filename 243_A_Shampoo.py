V, A, B, C = map(int, input().split())
s = V % (A + B + C)
if s < A:
    print("F")
elif s < A + B:
    print("M")
else:
    print("T")
