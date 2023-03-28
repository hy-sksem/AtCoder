from functools import lru_cache


@lru_cache
def solve(x):
    if x == 0:
        return 1
    return solve(x // 2) + solve(x // 3)


print(solve(int(input())))
