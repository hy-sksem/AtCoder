# https://atcoder.jp/contests/abc141/tasks/abc141_b

S = input()

for i, s in enumerate(S):
    if (i+1) % 2 == 0:
        if s == "R":
            print("No")
            exit()
    else:
        if s == "L":
            print("No")
            exit()
print("Yes")