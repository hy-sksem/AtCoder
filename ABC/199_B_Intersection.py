n = int(input())
a_l = map(int, input().split())
b_l = map(int, input().split())

ans = set(range(10000))
for a, b in zip(a_l, b_l):
    tmp = set(range(a,b+1))
    ans = ans & tmp
print(len(ans)) 
