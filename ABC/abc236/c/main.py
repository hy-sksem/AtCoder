N, M = map(int, input().split())
S = list(input().split())
T = list(input().split())

both = set(S).intersection(T)

for s in S:
    if s in both:
        print("Yes")
    else:
        print("No")
