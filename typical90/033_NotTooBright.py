H, W = map(int, input().split())

h = (H + 1) // 2
w = (W + 1) // 2
print(H * W if H == 1 or W == 1 else h * w)
