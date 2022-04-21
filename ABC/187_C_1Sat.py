N = int(input())
S = [input() for _ in range(N)]
a = set()
b = set()
for s in S:
    b.add(s[1:]) if s[0] == '!' else a.add(s)

ab = list(a & b)
print(ab[0]) if len(ab) > 0 else print('satisfiable')
