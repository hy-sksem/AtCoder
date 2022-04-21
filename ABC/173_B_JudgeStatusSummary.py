# https://atcoder.jp/contests/abc173/tasks/abc173_b

n = int(input())
s = list(input() for i in range(n))

print("AC x {}".format(s.count("AC")))
print("WA x {}".format(s.count("WA")))
print("TLE x {}".format(s.count("TLE")))
print("RE x {}".format(s.count("RE")))