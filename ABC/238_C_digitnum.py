N = int(input())
ans = N * (N + 1) // 2

if N >= 10:
    ans -= 9 * (N - 9)
if N >= 100:
    ans -= 90 * (N - 99)
if N >= 1000:
    ans -= 900 * (N - 999)
if N >= 10000:
    ans -= 9000 * (N - 9999)
if N >= 100000:
    ans -= 90000 * (N - 99999)
if N >= 1000000:
    ans -= 900000 * (N - 999999)
if N >= 10000000:
    ans -= 9000000 * (N - 9999999)
if N >= 100000000:
    ans -= 90000000 * (N - 99999999)
if N >= 1000000000:
    ans -= 900000000 * (N - 999999999)
if N >= 10000000000:
    ans -= 9000000000 * (N - 9999999999)
if N >= 100000000000:
    ans -= 90000000000 * (N - 99999999999)
if N >= 1000000000000:
    ans -= 900000000000 * (N - 999999999999)
if N >= 10000000000000:
    ans -= 9000000000000 * (N - 9999999999999)
if N >= 100000000000000:
    ans -= 90000000000000 * (N - 99999999999999)
if N >= 1000000000000000:
    ans -= 900000000000000 * (N - 999999999999999)
if N >= 10000000000000000:
    ans -= 9000000000000000 * (N - 9999999999999999)
if N >= 100000000000000000:
    ans -= 90000000000000000 * (N - 99999999999999999)
if N >= 1000000000000000000:
    ans -= 900000000000000000 * (N - 999999999999999999)

print(ans % 998244353)
