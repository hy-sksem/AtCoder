N = int(input())

t = list(range(1, 2 * N + 2))
print(1)
t.remove(1)
for i in range(N):
    aoki = int(input())
    t.remove(aoki)
    print(t.pop())
