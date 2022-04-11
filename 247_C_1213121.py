def func(f, n):
    return f + " " + n + f


N = int(input())
ans = ""
for i in range(1, N + 1):
    ans = func(ans, str(i))
print(ans.strip())
