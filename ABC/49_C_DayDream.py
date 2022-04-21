import re
s = input()
s = re.sub("eraser", "", s)
s = re.sub("erase", "", s)
s = re.sub("dreamer", "", s)
s = re.sub("dream", "", s)
print("YES") if s == "" else print("NO")