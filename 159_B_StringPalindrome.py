# https://atcoder.jp/contests/abc159/tasks/abc159_b

S = input()
f_l = int((len(S)-1)/2)
s_l = int((len(S)+3)/2)
first = S[0:f_l]
second = S[s_l-1:]
if first == second == second[::-1]:
    print("Yes")
else:
    print("No")