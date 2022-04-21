# https://atcoder.jp/contests/abc196/tasks/abc196_b

import re

x = input()
ans = re.sub(r"\.[0-9]*", "", x)
print(ans)