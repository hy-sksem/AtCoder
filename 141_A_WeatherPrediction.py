# https://atcoder.jp/contests/abc141/tasks/abc141_a

S = input()
weather = ["Sunny", "Cloudy", "Rainy"]

print(weather[weather.index(S)+1] if weather.index(S) != 2 else "Sunny")