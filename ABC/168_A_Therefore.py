# https://atcoder.jp/contests/abc168/tasks/abc168_a

n = input()
hon = ["2", "4", "5", "7", "9"]
pon = ["0", "1", "6", "8"]
bon = ["3"]
if n[-1] in hon:
    print("hon")
elif n[-1] in pon:
    print("pon")
elif n[-1] in bon:
    print("bon")