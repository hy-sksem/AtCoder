# https://atcoder.jp/contests/abc167/tasks/abc167_b

A, B, C, K = map(int, input().split())

ans = 0
if A >= K:
    print(1 * K)
    exit()
else:
    ans += 1 * A
    if A + B >= K:
        print(ans)
        exit()
    else:
        ans += -1 * (K - A - B)
        print(ans)
