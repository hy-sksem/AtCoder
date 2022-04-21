# https://atcoder.jp/contests/abc192/tasks/abc192_b

S = input()

for i, s in enumerate(S, start=1):
    if i % 2 == 0:
        if s.isupper():
            continue
        else:
            print("No")
            exit()
    else:
        if s.islower():
            continue
        else:
            print("No")
            exit()
print("Yes")
