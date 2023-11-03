N = int(input())

while True:
    a, b, c = int(str(N)[0]), int(str(N)[1]), int(str(N)[2])
    if a * b == c:
        break
    else:
        N += 1
print(N)
