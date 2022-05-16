N = int(input())
B = list(map(int, input().split()))
R = list(map(int, input().split()))

print(sum(B) / N + sum(R) / N)
