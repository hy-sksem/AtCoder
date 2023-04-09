# chess

S = input()

B = []
K = -1
R = []
for i, s in enumerate(S):
    if s == "B":
        B.append(i)
    elif s == "K":
        K = i
    elif s == "R":
        R.append(i)

if B[0] % 2 != B[1] % 2 and R[0] < K < R[1]:
    print("Yes")
else:
    print("No")
