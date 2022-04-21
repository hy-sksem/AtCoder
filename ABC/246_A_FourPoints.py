X1, Y1 = map(int, input().split())
X2, Y2 = map(int, input().split())
X3, Y3 = map(int, input().split())

X4 = X1 if X2 == X3 else X2 if X1 == X3 else X3
Y4 = Y1 if Y2 == Y3 else Y2 if Y1 == Y3 else Y3

print(X4, Y4)
