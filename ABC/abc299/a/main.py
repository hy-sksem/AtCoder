import re

N = int(input())
S = input()

print("in" if re.search(r"\|.*\*+.*\|", S) else "out")
