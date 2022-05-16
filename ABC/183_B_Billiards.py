# https://atcoder.jp/contests/abc183/tasks/abc183_b

sx, sy, gx, gy = map(int, input().split())

print(sx + (gx - sx) * (sy / (gy + sy)))
