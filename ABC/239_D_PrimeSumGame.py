A, B, C, D =map(int, input().split())

prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

w = [False] * 210

for i in range(A+C, B+D+1):
    if i in prime:
        w[i] = True

cnt = 0
for i in range(A+C, B+D+1):
    if not w[i]:
        cnt += 1
    else:
        cnt = 0
    if cnt >= (D-C+1):
        print("Takahashi")
        exit()
print("Aoki")