first = ("H", "D", "C", "S")
second = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K")

d = set()
N = int(input())
ans = "Yes"
for i in range(N):
    s = input()
    if s[0] in first and s[1] in second:
        if s not in d:
            d.add(s)
        else:
            ans = "No"
    else:
        ans = "No"
print(ans)
