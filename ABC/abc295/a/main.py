N = int(input())
W = list(input().split())
# and, not, that, the, you
yes = ["and", "not", "that", "the", "you"]

for w in W:
    if w in yes:
        exit(print("Yes"))
print("No")
