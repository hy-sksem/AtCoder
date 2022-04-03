def hantei(s):
    dep = 0
    for i in range(len(s)):
        if s[i] == "(":
            dep += 1
        else:
            dep -= 1
        if dep < 0:
            return False
    return True if dep == 0 else False


N = int(input())
for i in range(0, 1 << N):
    candidate = ""
    for j in range(N - 1, -1, -1):
        if i & (1 << j) == 0:
            candidate += "("
        else:
            candidate += ")"
    if hantei(candidate):
        print(candidate)
