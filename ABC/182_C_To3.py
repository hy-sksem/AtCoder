# https://atcoder.jp/contests/abc182/tasks/abc182_c

N = input()
nums = list(int(i) for i in N)

ans = -1
if sum(nums) % 3 == 0:
    print(0)
elif sum(nums) % 3 == 1 and len(nums) != 1:
    cnt = 0
    for n in nums:
        if n % 3 == 2:
            cnt += 1
            if cnt == 2 and len(nums) > 2:
                ans = 2
        elif n % 3 == 1:
            print(1)
            exit()
    print(ans)
    exit()
elif sum(nums) % 3 == 2 and len(nums) != 1:
    cnt = 0
    for n in nums:
        if n % 3 == 1:
            cnt += 1
            if cnt == 2 and len(nums) > 2:
                ans = 2
        elif n % 3 == 2:
            print(1)
            exit()
    print(ans)
    exit()
else:
    print(-1)
    exit()
