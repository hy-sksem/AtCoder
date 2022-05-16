# https://atcoder.jp/contests/abc171/tasks/abc171_a

import re

a = input()
print("A") if re.match(r"[A-Z]", a) else print("a")
