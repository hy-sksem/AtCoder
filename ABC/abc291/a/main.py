S = input()
for i, s in enumerate(S, start=1):
    if s.isupper():
        exit(print(i))
