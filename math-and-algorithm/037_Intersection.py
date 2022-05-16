def cross(ax, ay, bx, by):
    return ax * by - ay * bx


x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
x4, y4 = map(int, input().split())

cross1 = cross(x2 - x1, y2 - y1, x3 - x1, y3 - y1)
cross2 = cross(x2 - x1, y2 - y1, x4 - x1, y4 - y1)
cross3 = cross(x4 - x3, y4 - y3, x1 - x3, y1 - y3)
cross4 = cross(x4 - x3, y4 - y3, x2 - x3, y2 - y3)

if cross1 == 0 and cross2 == 0 and cross3 == 0 and cross4 == 0:
    A = (x1, y1)
    B = (x2, y2)
    C = (x3, y3)
    D = (x4, y4)
    if A > B:
        A, B = B, A
    if C > D:
        C, D = D, C
    if max(A, C) <= min(B, D):
        print("Yes")
    else:
        print("No")
else:
    divideAB = False
    divideCD = False
    if cross1 >= 0 and cross2 <= 0:
        divideAB = True
    if cross1 <= 0 and cross2 >= 0:
        divideAB = True
    if cross3 >= 0 and cross4 <= 0:
        divideCD = True
    if cross3 <= 0 and cross4 >= 0:
        divideCD = True

    if divideAB and divideCD:
        print("Yes")
    else:
        print("No")
