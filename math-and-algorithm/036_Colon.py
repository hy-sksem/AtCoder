import math

A, B, H, M = map(int, input().split())

AngleH = H * 30 + M * 0.5
AngleM = M * 6
Hx = A * math.cos(math.radians(AngleH))
Hy = A * math.sin(math.radians(AngleH))
Mx = B * math.cos(math.radians(AngleM))
My = B * math.sin(math.radians(AngleM))

d = ((Hx - Mx) ** 2 + (Hy - My) ** 2) ** 0.5
print(d)
