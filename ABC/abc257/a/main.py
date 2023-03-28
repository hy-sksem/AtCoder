N, X = map(int, input().split())
st = ""

for i in range(26):
    for j in range(N):
        st += chr(ord("A") + i)
print(st[X - 1])
