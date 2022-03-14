N = int(input())
X = [None] * N
Y = [None] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())
S = input()

right_min, left_max = dict(), dict()
for i in range(N):
    if S[i] == "R":
        if Y[i] in left_max and X[i] < left_max[Y[i]]:
            print("Yes")
            exit()
    else:
        if Y[i] in right_min and right_min[Y[i]] < X[i]:
            print("Yes")
            exit()
    if S[i] == "R":
        if Y[i] in right_min:
            right_min[Y[i]] = min(X[i], right_min[Y[i]])
        else:
            right_min[Y[i]] = X[i]
    else:
        if Y[i] in left_max:
            left_max[Y[i]] = max(X[i], left_max[Y[i]])
        else:
            left_max[Y[i]] = X[i]
print("No")
