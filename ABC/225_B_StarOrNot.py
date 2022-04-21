N = int(input())
AB = [list(map(int, input().split())) for _ in range(N-1)]

T = [0] * (N+1)

for a, b in AB:
    T[a] += 1
    T[b] += 1

print("Yes") if (N-1) in T else print("No")
