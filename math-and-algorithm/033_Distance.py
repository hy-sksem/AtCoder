ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())

BAx = ax - bx
BAy = ay - by
BCx = cx - bx
BCy = cy - by
CAx = ax - cx
CAy = ay - cy
CBx = bx - cx
CBy = by - cy

pattern = 2
if BAx * BCx + BAy * BCy < 0:
    pattern = 1
elif CAx * CBx + CAy * CBy < 0:
    pattern = 3

ans = 0
