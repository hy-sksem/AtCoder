S = list(map(str, input()))
T = list(map(str, input()))

diffs = set()
for s, t in zip(S, T):
    diff = ord(t) - ord(s) if ord(t) >= ord(s) else ord(t) + 26 - ord(s)
    diffs.add(diff)

print("Yes" if len(diffs) == 1 else "No")
